#!/usr/bin/env python3
import os

from lxcraft import Plan
from lxcraft.debian import AptPackages
from lxcraft.path import Directory, FileContent
from lxcraft.user import User

USERNAME = "wwwkindos"


def custom_file(
    filename: str, user: str = USERNAME, group: str = USERNAME, mode: int = 0o644
):
    return FileContent(
        filename,
        owner_user=user,
        owner_group=group,
        replace={"{USERNAME}": USERNAME},
        mode=mode,
    )


def test_fastapi_uvicorn_gunicorn_supervisor():
    def supervisorctl_reload():
        os.system("supervisorctl reread && supervisorctl update")

    plan_components = [
        AptPackages(["systemctl", "supervisor"]),
        AptPackages(["python3-fastapi", "uvicorn", "gunicorn"]),
        User(USERNAME),
        Directory(f"/run/user/{USERNAME}"),
        Directory(f"/var/log/{USERNAME}/"),
        custom_file(f"/home/{USERNAME}/main.py"),
        custom_file(f"/home/{USERNAME}/gunicorn_start", mode=0o755),
        custom_file(
            f"/etc/supervisor/conf.d/{USERNAME}.conf", "root", "root"
        ).on_change(supervisorctl_reload),
    ]
    with Plan(plan_components) as plan:
        plan.execute()
