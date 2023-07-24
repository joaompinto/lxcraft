import os

from lxcraft import Plan
from lxcraft.debian import AptPackages


def test_package_install():
    Plan([AptPackages(["nginx"])]).execute()
    assert AptPackages.is_installed("nginx")


def test_package_install_multiple():
    os.system("apt remove nginx")
    test_package_install()
