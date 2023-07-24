import pwd

from lxcraft import Plan
from lxcraft.user import User

USERNAME = "lxcraft"


def test_user_add():
    Plan(User(USERNAME)).execute()
    assert pwd.getpwnam(USERNAME)
