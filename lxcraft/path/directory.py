import os
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Directory:
    """Directory to be created or removed"""

    path: str
    must_not_exist: bool = False

    def get_actions(self):
        if self.must_not_exist and Path(self.path).exists():
            return [self.rmtree]
        elif not self.must_not_exist and not Path(self.path).exists():
            return [self.makedirs]

    def rmtree(self):
        shutil.rmtree(self.path)

    def makedirs(self):
        os.makedirs(self.path, exist_ok=True)
