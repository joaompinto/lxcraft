from lxcraft import Plan, User
from lxcraft.user import user_exists

USERNAME = "lxcraft"


def test_user_remove():
    Plan(
        "ensure the user is not present", [User(USERNAME, must_be_present=False)]
    ).run()
    assert not user_exists(USERNAME)


def test_user_add():
    Plan("ensure the user is not present", [User(USERNAME)]).run()
    assert user_exists(USERNAME)


def test_user_mutiple():
    test_user_remove()
    test_user_add()
    test_user_remove()
