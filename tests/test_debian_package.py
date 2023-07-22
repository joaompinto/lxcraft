from lxcraft import Plan
from lxcraft.debian import APTPackages


def test_package_install():
    plan = Plan(
        "ensure nginx is uninstalled", [APTPackages(["nginx"], must_be_installed=False)]
    )
    plan.run()
    assert len(plan.preview()) == 0

    # re-running should trigger 0 actions
    assert len(plan.run()) == 0

    plan = Plan(
        "ensure nginx is installed", [APTPackages(["nginx"], must_be_installed=True)]
    )

    # something was executed
    assert len(plan.run()) == 1

    # nothing should be pending after running the plan
    assert len(plan.preview()) == 0
