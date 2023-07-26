from dataclasses import dataclass
from pathlib import Path

import lxcraft


@dataclass
class Directory(lxcraft.Resource):
    """Directory to be created or removed"""

    path: str

    def create(self):
        Path(self.path).mkdir(parents=True, exist_ok=True)

    def destroy(self):
        Path(self.path).rmdir()

    def is_created(self):
        return Path(self.path).exists()

    def is_consistent(self):
        return Path(self.path).is_dir()
