from pathlib import Path

from lxcraft import Plan
from lxcraft.path import Directory

DIRNAME = "/run/user/www-data"


def test_directory_create():
    with Plan([Directory(DIRNAME)]) as plan:
        plan.execute()
        assert Path(DIRNAME).is_dir()
