#!/usr/bin/env python3
from lxcraft import Plan, User
from lxcraft.debian import APTPackages, SystemdService
from lxcraft.path import Directory, FileContent
from lxcraft.python import PipPackages

USERNAME = "wwwkindos"


def test_fastapi_uvicorn_gunicorn_supervisor():
    update_supervisor_config_plan = Plan(
        "update supervisor",
        [SystemdService("supervisor", must_reread=True, must_update=True)],
    ).run()

    plan_components = [
        PipPackages(["fastapi", "uvicorn", "gunicorn"]),
        APTPackages(["supervisor"]),
        User(USERNAME),
        Directory(f"/run/user/{USERNAME}"),
        FileContent(f"/home/{USERNAME}/main.py", "tests/template/main.py"),
        FileContent(
            f"/etc/supervisor/conf.d/{USERNAME}.conf",
            f"tests/template/{USERNAME}.conf",
            replace={"{USER}": USERNAME},
        ).on_change(update_supervisor_config_plan),
    ]
    Plan("my-plan", plan_components).run()
