#!/usr/bin/env python3
from lxcraft import Plan
from lxcraft.debian import AptPackages
from lxcraft.path import Directory, FileContent
from lxcraft.python import PipPackages
from lxcraft.user import User

USERNAME = "wwwkindos"


def test_fastapi_uvicorn_gunicorn_supervisor():
    plan_components = [
        PipPackages(["fastapi", "uvicorn", "gunicorn"]),
        AptPackages(["supervisor"]),
        User(USERNAME),
        Directory(f"/run/user/{USERNAME}"),
        FileContent(
            f"/home/{USERNAME}/main.py",
            "tests/template/main.py",
            owner_user=USERNAME,
            owner_group=USERNAME,
        ),
        FileContent(
            f"/etc/supervisor/conf.d/{USERNAME}.conf",
            f"tests/template/{USERNAME}.conf",
            replace={"{USER}": USERNAME},
        ),
    ]
    Plan(plan_components).execute()
