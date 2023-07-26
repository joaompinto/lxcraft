import pwd

from lxcraft import Plan
from lxcraft.user import User

USERNAME = "lxcraft"

fields = {
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
    kwargs = {}
    for key, value in fields.items():
        kwargs[key] = value
        Plan(User(**kwargs)).execute()
        assert pwd.getpwnam(USERNAME)

    # Idempotency test
    Plan(User(**kwargs)).execute()
    assert pwd.getpwnam(USERNAME)

    Plan(User(*kwargs)).destroy()
