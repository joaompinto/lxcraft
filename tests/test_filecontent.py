from pathlib import Path

import pytest

from lxcraft import Plan
from lxcraft.path import FileContent

FileContent.set_templates_directory("tests/templates")
SOURCE_PATH = "tests/templates/test.txt"
TARGET_PATH = "/tmp/test.txt"


def test_filecontent_create():
    with Plan([FileContent(TARGET_PATH)]) as plan:
        plan.execute()
        target_text = Path(TARGET_PATH).read_text()
        assert "this is a {word} test\n" == target_text

    with Plan([FileContent(TARGET_PATH, SOURCE_PATH)]) as plan:
        plan.execute()
        target_text = Path(TARGET_PATH).read_text()
        assert "this is a {word} test\n" == target_text

    with pytest.raises(FileNotFoundError):
        with Plan([FileContent(TARGET_PATH, "missing_file")]) as plan:
            plan.execute()


def test_filecontent_create_replace():
    with Plan([FileContent(TARGET_PATH, replace={"{word}": "bananas"})]) as plan:
        plan.execute()
        target_text = Path(TARGET_PATH).read_text()
        assert "bananas" in target_text


def test_filecontent_chmod():
    with Plan([FileContent(TARGET_PATH, mode=0o600)]) as plan:
        plan.execute()
        assert oct(Path(TARGET_PATH).stat().st_mode & 0o777) == "0o600"


def test_filencontnet_chown():
    # Adjust owner on creation
    with Plan([FileContent(TARGET_PATH, owner_user="daemon")]) as plan:
        plan.execute()
        assert Path(TARGET_PATH).stat().st_uid == 1

    # Adjust owner after creation
    Plan([FileContent(TARGET_PATH)]).execute()
    with Plan([FileContent(TARGET_PATH, owner_user="daemon")]) as plan:
        plan.execute()
        assert Path(TARGET_PATH).stat().st_uid == 1

    Plan([FileContent(TARGET_PATH)]).execute()
    with Plan([FileContent(TARGET_PATH, owner_group="bin")]) as plan:
        plan.execute()
        assert Path(TARGET_PATH).stat().st_gid == 2
