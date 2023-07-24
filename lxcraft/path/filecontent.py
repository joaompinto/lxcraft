import grp
import os
import pwd
from dataclasses import dataclass, field
from pathlib import Path

import lxcraft


@dataclass
class FileContent(lxcraft.PlanElement):
    """Create file with content"""

    target_path: str
    source_path: str = ""
    owner_user: str = ""
    owner_group: str = ""
    mode: int = 0o644
    replace: dict = field(default_factory=dict)
    templates_directory = "templates"

    @staticmethod
    def set_templates_directory(directory: str):
        FileContent.templates_directory = directory

    def get_source_text(self):
        if self.source_path:
            source_path = Path(self.source_path)
        else:
            filename = Path(self.target_path).name
            source_path = Path(self.templates_directory) / filename
        if source_path.exists():
            source_text = source_path.read_text()
        else:
            raise FileNotFoundError(f"Source file {source_path} not found")

        replaced_text = source_text
        for key, value in self.replace.items():
            replaced_text = replaced_text.replace(key, value)
        return replaced_text

    def content_differs(self):
        try:
            target_text = Path(self.target_path).read_text()
        except FileNotFoundError:
            return True
        return self.get_source_text() != target_text

    def owner_differs(self):
        if not self.owner_user and not self.owner_group:
            return False

        try:
            current_uid = Path(self.target_path).stat().st_uid
            current_gid = Path(self.target_path).stat().st_gid
        except FileNotFoundError:  # The target file is not yet on the system
            return True
        if self.owner_user and pwd.getpwnam(self.owner_user).pw_uid != current_uid:
            return True
        if self.owner_group and grp.getgrnam(self.owner_group).gr_gid != current_gid:
            return True

    def mode_differs(self):
        try:
            return self.mode != Path(self.target_path).stat().st_mode & 0o777
        except FileNotFoundError:
            return True

    def get_actions(self):
        return self.action_engine(
            {
                self.content_differs: self.create,
                self.owner_differs: self.chown,
                self.mode_differs: self.chmod,
            }
        )

    def create(self):
        Path(self.target_path).write_text(self.get_source_text())

    def chown(self):
        if self.owner_user == "":
            uid = os.getuid()
        else:
            uid = pwd.getpwnam(self.owner_user).pw_uid
        if self.owner_group == "":
            gid = os.getgid()
        else:
            gid = grp.getgrnam(self.owner_group).gr_gid
        os.chown(self.target_path, uid, gid)

    def chmod(self):
        os.chmod(self.target_path, self.mode)

    def destroy(self):
        os.remove(self.target_path)
