import grp
import pwd
from dataclasses import dataclass, field

import lxcraft


@dataclass
class User(lxcraft.Resource):
    username: str
    gecos: str | None = None
    password: str | None = None
    shell: str = "/usr/sbin/nologin"
    home: str | None = None
    uid: int | None = None
    gid: int | None = None
    groups: list | None = field(default_factory=list)
    create_home: bool = True

    def create(self):
        self.create_user()

    def destroy(self):
        lxcraft.system(f"userdel {self.username}")

    def is_created(self):
        try:
            pwd.getpwnam(self.username)
        except KeyError:
            return False
        return True

    def is_consistent(self):
        user_data = pwd.getpwnam(self.username)
        if self.gecos is not None and self.gecos != user_data.pw_gecos:
            return False
        if self.shell is not None and self.shell != user_data.pw_shell:
            return False
        if self.home is not None and self.home != user_data.pw_dir:
            return False
        if self.uid is not None and self.uid != user_data.pw_uid:
            return False
        if self.gid is not None and self.gid != user_data.pw_gid:
            return False
        if self.groups is not None and self.groups != self.current_user_groups():
            return False
        return True

    def current_user_groups(self):
        return [g.gr_name for g in grp.getgrall() if self.username in g.gr_mem]

    def create_user(self):
        cmd = f"useradd {self.username}"
        if self.gecos is not None:
            cmd += f" -c {self.gecos}"
        if self.password is not None:
            cmd += f" -p {self.password}"
        if self.shell is not None:
            cmd += f" -s {self.shell}"
        if self.home is not None:
            cmd += f" -d {self.home}"
        if self.uid is not None:
            cmd += f" -u {self.uid}"
        if self.gid is not None:
            cmd += f" -g {self.gid}"
        if self.groups:
            cmd += f" -G {','.join(self.groups)}"
        if self.create_home:
            cmd += " -m"
        lxcraft.system(cmd)
