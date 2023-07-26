import pytest

from lxcraft import Plan
from lxcraft.debian import AptPackages


def test_apt_package():
    with Plan([AptPackages(["nginx"])]) as plan:
        plan.execute()
        Plan([AptPackages(["nginx"])]).execute()  # test idempotency

    with pytest.raises(Exception, match=r"Command terminated with non zero exit code"):
        Plan(AptPackages(["blaldderandom"])).execute()
