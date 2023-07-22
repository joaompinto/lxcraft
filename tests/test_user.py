from lxcraft import Plan, User
from lxcraft.user import user_exists


def test_user_remove():
    Plan(
        "ensure the user is not present", [User("lxcraf", must_be_present=False)]
    ).run()
    assert not user_exists("lxcraf")


def test_user_add():
    assert not user_exists("lxcraf")
    Plan("ensure the user is not present", [User("lxcraf", must_be_present=True)]).run()
    assert user_exists("lxcraf")
