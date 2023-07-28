import grp
import os
import pwd
from dataclasses import dataclass
from pathlib import Path

import lxcraft


@dataclass
class Directory(lxcraft.Resource):
    """Directory in the filesystem"""

    path: str
    owner_user: str = ""
    owner_group: str = ""
    mode: int = 0o755

    def create(self):
        Path(self.path).mkdir(parents=True, exist_ok=True)
        if self.owner_user != "" or self.owner_group != "":
            self.chown()
        if self.mode:
            self.chmod()

    def destroy(self):
        Path(self.path).rmdir()

    def is_created(self):
        return Path(self.path).exists()

    def is_consistent(self):
        return Path(self.path).is_dir() and self.mode_matches() and self.owner_matches()

    def owner_matches(self):
        current_uid = Path(self.path).stat().st_uid
        current_gid = Path(self.path).stat().st_gid
        if self.owner_user and pwd.getpwnam(self.owner_user).pw_uid != current_uid:
            return False
        if self.owner_group and grp.getgrnam(self.owner_group).gr_gid != current_gid:
            return False
        return True

    def mode_matches(self):
        return self.mode == Path(self.path).stat().st_mode & 0o777

    def chown(self):
        if self.owner_user == "":
            uid = os.getuid()
        else:
            uid = pwd.getpwnam(self.owner_user).pw_uid
        if self.owner_group == "":
            gid = os.getgid()
        else:
            gid = grp.getgrnam(self.owner_group).gr_gid
        os.chown(self.path, uid, gid)

    def chmod(self):
        os.chmod(self.path, self.mode)
