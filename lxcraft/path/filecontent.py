import grp
import os
import pwd
from dataclasses import dataclass, field
from pathlib import Path

from lxcraft.base import BaseAction, action_engine


@dataclass
class FileContent(BaseAction):
    """Create file with content"""

    target_path: str
    source_path: str
    owner_user: str = ""
    owner_group: str = ""
    mode: int = 0o644
    replace: dict = field(default_factory=dict)

    def content_differs(self):
        source_text = Path(self.source_path).read_text()
        try:
            target_text = Path(self.target_path).read_text()
        except FileNotFoundError:
            return True
        return source_text != target_text

    def owner_differs(self):
        if (
            self.owner_user
            and pwd.getpwnam(self.owner_user).pw_uid
            != Path(self.target_path).stat().st_uid
        ):
            return True
        if (
            self.owner_group
            and grp.getgrnam(self.owner_group).gr_gid
            != Path(self.target_path).stat().st_gid
        ):
            return True

    def mode_differs(self):
        try:
            return self.mode != Path(self.target_path).stat().st_mode & 0o777
        except FileNotFoundError:
            return True

    def get_actions(self):
        return action_engine(
            {
                self.content_differs: self.create,
                self.owner_differs: self.chown,
                self.mode_differs: self.chmod,
            }
        )

    def create(self):
        text = Path(self.source_path).read_text()
        Path(self.target_path).write_text(text)

    def chown(self):
        os.chown(
            self.target_path,
            pwd.getpwnam(self.owner_user).pw_uid,
            grp.getgrnam(self.owner_group).gr_gid,
        )

    def chmod(self):
        os.chmod(self.target_path, self.mode)
