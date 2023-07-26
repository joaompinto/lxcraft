import pytest

from lxcraft import Plan
from lxcraft.python import PipPackages


def test_pip_package():
    TEST_PACKAGE = "docopt"

    with Plan([PipPackages([TEST_PACKAGE])]) as plan:
        plan.execute()
        Plan([PipPackages([TEST_PACKAGE])]).execute()  # test idempotency
        assert PipPackages.is_installed(TEST_PACKAGE)

    with pytest.raises(Exception, match=r"Command terminated with non zero exit code"):
        Plan([PipPackages([".blaldderandom"])]).execute()
