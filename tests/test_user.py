from lxcraft import Plan, User
from lxcraft.user import user_exists

USERNAME = "lxcraft"


def test_user_remove():
    Plan("ensure the user is not present", [User(USERNAME)]).run()
    assert user_exists(USERNAME)
