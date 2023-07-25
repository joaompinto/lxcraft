#!/usr/bin/env python3
import os

from lxcraft import Plan
from lxcraft.debian import AptPackages
from lxcraft.path import Directory, FileContent
from lxcraft.python import PipPackages
from lxcraft.user import User

USERNAME = "wwwkindos"


def custom_file(
    filename: str, user: str = USERNAME, group: str = USERNAME, mode: int = 0o644
):
    return FileContent(
        filename,
        owner_user=user,
        owner_group=group,
        replace={"{USER}": USERNAME},
        mode=mode,
    )


def supervisorctl_reload():
    os.system("supervisorctl reread && supervisorctl update")


def test_fastapi_uvicorn_gunicorn_supervisor():
    plan_components = [
        PipPackages(["fastapi", "uvicorn", "gunicorn"]),
        AptPackages(["supervisor"]),
        User(USERNAME),
        Directory(f"/run/user/{USERNAME}"),
        custom_file(f"/home/{USERNAME}/main.py"),
        custom_file(f"/home/{USERNAME}/gunicorn_start", mode=0o755),
        custom_file(
            f"/etc/supervisor/conf.d/{USERNAME}.conf", "root", "root"
        ).on_change(supervisorctl_reload),
    ]
    with Plan(plan_components) as plan:
        plan.execute()
