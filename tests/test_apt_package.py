import pytest

from lxcraft import Plan
from lxcraft.debian import AptPackages


def test_apt_package_ok():
    with Plan([AptPackages(["nginx"])]) as plan:
        plan.execute()
        Plan([AptPackages(["nginx"])]).execute()  # test idempotency


def test_apt_package_fail():
    with pytest.raises(Exception, match=r"Command terminated with non zero exit code"):
        Plan([AptPackages(["blaldderandom"])]).execute()
