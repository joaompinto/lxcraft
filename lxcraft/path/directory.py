import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Directory:
    """Directory to be created or removed"""

    path: str

    def get_actions(self):
        if not Path(self.path).exists():
            return [self.makedirs]

    def makedirs(self):
        os.makedirs(self.path, exist_ok=True)
