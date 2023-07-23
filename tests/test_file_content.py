from pathlib import Path

from lxcraft import Plan
from lxcraft.path import FileContent

TARGET_PATH = "/tmp/test.txt"
SOURCE_PATH = "tests/template/test.txt"


def test_filecontent_create():
    Path(TARGET_PATH).unlink(missing_ok=True)
    Plan(
        "ensure the directory is present", [FileContent(TARGET_PATH, SOURCE_PATH)]
    ).run()
    target_text = Path(TARGET_PATH).read_text()
    source_text = Path(SOURCE_PATH).read_text()
    assert source_text
    assert source_text == target_text
    assert oct(Path(TARGET_PATH).stat().st_mode & 0o777) == "0o644"


def test_filecontent_chmod():
    Plan(
        "ensure the directory is present",
        [FileContent(TARGET_PATH, SOURCE_PATH, mode=0o600)],
    ).run()
    assert oct(Path(TARGET_PATH).stat().st_mode & 0o777) == "0o600"


def test_filencontnet_chown():
    Plan(
        "ensure the directory is present",
        [FileContent(TARGET_PATH, SOURCE_PATH, owner_user="daemon", owner_group="bin")],
    ).run()
    assert Path(TARGET_PATH).stat().st_uid == 1
    assert Path(TARGET_PATH).stat().st_gid == 2
