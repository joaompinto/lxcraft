import pwd

import pytest

from lxcraft import Plan
from lxcraft.user import User

USERNAME = "lxcraft"


def test_user_add():
    with Plan(User(USERNAME)) as plan:
        plan.execute()
        assert pwd.getpwnam(USERNAME)

    with Plan(
        User(
            USERNAME,
            "geocs",
            "password",
            "/bin/bash",
            f"/home/{USERNAME}",
            2000,
            1,
            ["root"],
            True,
        )
    ) as plan:
        plan.execute()
        assert pwd.getpwnam(USERNAME)
    with pytest.raises(Exception, match=r"Command terminated with non zero exit code"):
        Plan(User("")).execute()
