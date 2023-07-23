import os

from lxcraft import Plan
from lxcraft.debian import APTPackages


def test_package_install():
    Plan("ensure nginx is installed", [APTPackages(["nginx"])]).run()
    assert APTPackages.is_installed("nginx")


def test_package_install_multiple():
    os.system("apt remove nginx")
    test_package_install()
