from pathlib import Path

from lxcraft import Plan
from lxcraft.path import Directory

DIRNAME = "/run/user/www-data"


def test_directory_create():
    Plan([Directory(DIRNAME)]).execute()
    assert Path(DIRNAME).is_dir()


def test_user_mutiple():
    test_directory_create()
