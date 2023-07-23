import os
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path

from lxcraft.base import BaseAction


@dataclass
class File(BaseAction):
    """Create file with content"""

    target_path: str
    source_path: str
    owner: str = "root"
    mode: int = 0o644
    replace: dict = field(default_factory=dict)

    def get_current_uid(self):
        file_stat = Path(self.target_path).stat()
        return file_stat.st_uid

    def get_action(self):
        if Path(self.target_path).exists():
            source_text = Path(self.source_path).read_text()
            target_text = Path(self.target_path).read_text()
            if source_text == target_text:
                return
        return partial(self.create)

    def remove(self):
        os.unlink(self.target_path)

    def create(self):
        text = Path(self.source_path).read_text()
        Path(self.target_path).write_text(text)
