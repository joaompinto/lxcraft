import pwd
from typing import Any, Dict, TypedDict

from lxcraft import Plan
from lxcraft.user import User

USERNAME = "lxcraft"


class UserFields(TypedDict):
    username: str
    gecos: str | None
    password: str | None
    shell: str
    home: str | None
    uid: int | None
    gid: int | None
    groups: list | None


fields: UserFields = {
    "username": USERNAME,
    "gecos": "lxcraft",
    "password": "lxcraft",
    "shell": "/bin/sh",
    "home": "/home/lxcraft_test",
    "uid": 2000,
    "gid": 100,
    "groups": ["sudo"],
}


def test_user_add():
    kwargs: Dict[str, Any] = {}
    for key, value in fields.items():
        kwargs[key] = value
        Plan([User(**kwargs)]).execute()
        assert pwd.getpwnam(USERNAME)

    # Idempotency test
    Plan([User(**kwargs)]).execute()
    assert pwd.getpwnam(USERNAME)

    Plan([User(**kwargs)]).destroy()
