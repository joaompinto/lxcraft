import os
from dataclasses import dataclass
from functools import partial
from subprocess import getstatusoutput


@dataclass
class APTPackages:
    """List of packages that must be installed"""

    package_list: list[str]

    def get_actions(self):
        package_list = []
        for package in self.package_list:
            if self.is_installed(package):
                continue
            package_list.append(package)
        if not package_list:
            return
        return [partial(self.package_action, " ".join(package_list))]

    def package_action(self, package_list: str):
        rc = os.system(f"apt install -y {package_list}")
        if rc != 0:
            raise Exception(f"Command terminated with non zero exit code {rc}")

    @staticmethod
    def is_installed(package_name: str):
        rc, _ = getstatusoutput(f"dpkg -s {package_name}")
        return rc == 0
