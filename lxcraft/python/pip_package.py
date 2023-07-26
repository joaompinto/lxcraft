from dataclasses import dataclass
from subprocess import getstatusoutput

import lxcraft


@dataclass
class PipPackages(lxcraft.Resource):
    """List of packages that must be installed"""

    package_list: list[str]

    def create(self):
        package_list = " ".join(self.package_list)
        lxcraft.system(f"pip install {package_list}")

    def destroy(self):
        package_list = " ".join(self.package_list)
        lxcraft.system(f"pip uninstall -y {package_list}")

    def is_created(self):
        for package in self.package_list:
            if not self.is_installed(package):
                return False
        return True

    def is_consistent(self):
        # TODO: Add support for version checking
        return True

    @staticmethod
    def is_installed(package_name: str):
        rc, _ = getstatusoutput(f"pip show {package_name}")
        return rc == 0
