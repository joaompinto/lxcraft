#!/usr/bin/env python3
import lxcraft
from lxcraft import Plan
from lxcraft.debian import AptPackages
from lxcraft.path import Directory, FileContent
from lxcraft.user import User

USERNAME = "wwwkindos"


def template_file(
    filename: str, user: str = USERNAME, group: str = USERNAME, mode: int = 0o644
):
    return FileContent(
        filename,
        owner_user=user,
        owner_group=group,
        replace={"{USERNAME}": USERNAME},
        mode=mode,
    )


def supervisorctl_start_enable():
    lxcraft.system("systemctl start supervisor")


def supervisorctl_reload():
    lxcraft.system("systemctl start supervisor")
    lxcraft.system("supervisorctl reread && supervisorctl update")


Plan(
    [
        AptPackages(["systemctl", "supervisor"]).on_change(supervisorctl_start_enable),
        AptPackages(["python3-fastapi", "uvicorn", "gunicorn"]),
        User(USERNAME),
        Directory(f"/run/user/{USERNAME}", owner_user=USERNAME, owner_group=USERNAME),
        Directory(f"/var/log/{USERNAME}"),
        template_file(f"/home/{USERNAME}/main.py"),
        template_file(f"/home/{USERNAME}/gunicorn_start", mode=0o755),
        template_file(
            f"/etc/supervisor/conf.d/{USERNAME}.conf", "root", "root"
        ).on_change(supervisorctl_reload),
    ]
).execute()
