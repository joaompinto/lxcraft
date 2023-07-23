import os
import pwd
from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    gecos: str | None = None
    password: str | None = None
    shell: str = "/usr/sbin/nologin"
    home: str | None = None
    uid: int | None = None
    gid: int | None = None
    groups: list | None = field(default_factory=list)
    create_home: bool = True

    def get_actions(self):
        if not user_exists(self.username):
            return [self.create_user]

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
        os.system(cmd)

    def remove_user(self):
        cmd = f"userdel -r {self.username}"
        os.system(cmd)


def user_exists(username: str):
    try:
        pwd.getpwnam(username)
    except KeyError:
        return False
    return True
