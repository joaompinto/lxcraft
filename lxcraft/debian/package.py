import os
from dataclasses import dataclass
from functools import partial
from subprocess import getstatusoutput


@dataclass
class APTPackages:
    """List of packages that must be installed"""

    package_list: list[str]
    must_be_installed: bool = True

    def is_installed(selfl, package_name: str):
        rc, _ = getstatusoutput(f"dpkg -s {package_name}")
        return rc == 0

    def get_action(self):
        package_list = []
        for package in self.package_list:
            if self.is_installed(package):
                if self.must_be_installed:
                    continue
            else:
                if not self.must_be_installed:
                    continue
            package_list.append(package)
        if not package_list:
            return None
        action = "install" if self.must_be_installed else "remove"
        return partial(package_action, action, " ".join(package_list))


def package_action(action: str, package_list: str):
    rc = os.system(f"apt {action} -y {package_list}")
    if rc != 0:
        raise Exception(f"Command terminated with non zero exit code {rc}")
