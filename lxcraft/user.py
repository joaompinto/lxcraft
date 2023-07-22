import os
import pwd
from dataclasses import dataclass, field
from functools import partial


@dataclass
class User:
    username: str
    gecos: str = None
    password: str = None
    shell: str = "/bin/bash"
    home: str = None
    uid: int = None
    gid: int = None
    groups: list = field(default_factory=list)
    create_home: bool = True
    must_be_present: bool = True

    def get_action(self):
        print(self, self.username, self.must_be_present, user_exists(self.username))
        if self.must_be_present and not user_exists(self.username):
            return partial(create_user, self.username)
        if not self.must_be_present and user_exists(self.username):
            return partial(remove_user, self.username)


def user_exists(username: str):
    try:
        pwd.getpwnam(username)
    except KeyError:
        return False
    return True


def create_user(username: str):
    cmd = f"useradd {username}"
    os.system(cmd)


def remove_user(username: str):
    cmd = f"userdel -r {username}"
    os.system(cmd)
