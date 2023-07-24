import os
from dataclasses import dataclass
from pathlib import Path

import lxcraft


@dataclass
class Directory(lxcraft.PlanElement):
    """Directory to be created or removed"""

    path: str

    def get_actions(self):
        if not Path(self.path).exists():
            return [self.makedirs]

    def makedirs(self):
        os.makedirs(self.path, exist_ok=True)

    def destroy(self):
        os.removedirs(self.path)
