import os
import pwd
from dataclasses import dataclass, field
from functools import partial


@dataclass
class User:
    username: str
    gecos: str = None
    password: str = None
    shell: str = "/usr/sbin/nologin"
    home: str = None
    uid: int = None
    gid: int = None
    groups: list = field(default_factory=list)
    create_home: bool = True
    must_be_present: bool = True

    def get_action(self):
        if self.must_be_present and not user_exists(self.username):
            return partial(self.create_user)
        if not self.must_be_present and user_exists(self.username):
            return partial(self.remove_user)

    def create_user(self):
        cmd = f"useradd {self.username}"
        if self.gecos:
            cmd += f" -c {self.gecos}"
        if self.password:
            cmd += f" -p {self.password}"
        if self.shell:
            cmd += f" -s {self.shell}"
        if self.home:
            cmd += f" -d {self.home}"
        if self.uid:
            cmd += f" -u {self.uid}"
        if self.gid:
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
