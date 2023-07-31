from pathlib import Path

from lxcraft import Plan
from lxcraft.path import Directory

DIRNAME = "/run/user/www-data"


def test_directory_create():
    with Plan([Directory(DIRNAME)]) as plan:
        plan.execute()
        assert Path(DIRNAME).is_dir()

        Plan([Directory(DIRNAME, owner_user="bin")]).execute()
        Plan([Directory(DIRNAME, owner_group="bin")]).execute()

        Plan([Directory(DIRNAME, "bin", "bin", 0o755)]).execute()
