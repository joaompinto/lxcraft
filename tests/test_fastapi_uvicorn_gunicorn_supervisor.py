#!/usr/bin/env python3
from lxcraft import Plan, User
from lxcraft.debian import APTPackages, SystemdService
from lxcraft.path import Directory, File
from lxcraft.python import PipPackages

USERNAME = "wwwkindos"


def test_fastapi_uvicorn_gunicorn_supervisor():
    def update_supervisor_config():
        Plan(
            "update supervisor",
            [SystemdService("supervisor", must_reread=True, must_update=True)],
        ).run()

    plan_components = [
        PipPackages(["fastapi", "uvicorn", "gunicorn"]),
        APTPackages(["supervisor"]),
        User(USERNAME),
        Directory(f"/run/user/{USERNAME}"),
        File(f"/home/{USERNAME}/main.py", "tests/template/main.py"),
        File(
            f"/etc/supervisor/conf.d/{USERNAME}.conf",
            f"tests/template/{USERNAME}.conf",
            replace={"{USER}": USERNAME},
        ).on_change(update_supervisor_config),
    ]
    Plan("my-plan", plan_components).run()
