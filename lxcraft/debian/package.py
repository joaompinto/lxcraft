import os
from dataclasses import dataclass
from functools import partial
from subprocess import getstatusoutput


@dataclass
class APTPackages:
    """List of packages that must be installed"""

    package_list: list[str]
    must_be_present: bool = True

    def get_actions(self):
        package_list = []
        for package in self.package_list:
            if self.must_be_present and self.is_installed(package):
                continue
            if not self.must_be_present and not self.is_installed(package):
                continue
            package_list.append(package)
        if not package_list:
            return
        action = "install" if self.must_be_present else "remove"
        return [partial(self.package_action, action, " ".join(package_list))]

    def package_action(self, action: str, package_list: str):
        rc = os.system(f"apt {action} -y {package_list}")
        if rc != 0:
            raise Exception(f"Command terminated with non zero exit code {rc}")

    @staticmethod
    def is_installed(package_name: str):
        rc, _ = getstatusoutput(f"dpkg -s {package_name}")
        return rc == 0
