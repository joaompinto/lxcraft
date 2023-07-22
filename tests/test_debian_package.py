from lxcraft import Plan
from lxcraft.debian import APTPackages
from lxcraft.debian.package import is_installed


def test_package_install():
    Plan(
        "ensure nginx is installed", [APTPackages(["nginx"], must_be_present=True)]
    ).run()
    assert is_installed("nginx")


def test_package_remove():
    Plan(
        "ensure nginx is uninstalled", [APTPackages(["nginx"], must_be_present=False)]
    ).run()
    assert not is_installed("nginx")


def test_package_install_multiple():
    test_package_remove()
    test_package_install()
    test_package_remove()
