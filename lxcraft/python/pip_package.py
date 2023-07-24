import os
from dataclasses import dataclass
from subprocess import getstatusoutput

import lxcraft


@dataclass
class PipPackages(lxcraft.PlanElement):
    """List of packages that must be installed"""

    package_list: list[str]

    def get_actions(self):
        self.missing_package_list = []
        for package in self.package_list:
            if self.is_installed(package):
                continue
            self.missing_package_list.append(package)
        if self.missing_package_list:
            return self.install_missing()

    def install_missing(self):
        package_list = " ".join(self.missing_package_list)
        rc = os.system(f"pip install {package_list}")
        if rc != 0:
            raise Exception(f"Command terminated with non zero exit code {rc}")

    @staticmethod
    def is_installed(package_name: str):
        rc, _ = getstatusoutput(f"pip show {package_name}")
        return rc == 0
