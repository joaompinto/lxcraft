import os
from dataclasses import dataclass
from functools import partial
from subprocess import getstatusoutput


@dataclass
class PipPackages:
    """List of packages that must be installed"""

    package_list: list[str]
    must_be_present: bool = True

    def get_actions(self):
        package_list = []
        for package in self.package_list:
            if self.must_be_present and is_installed(package):
                continue
            if not self.must_be_present and not is_installed(package):
                continue
            package_list.append(package)
        if not package_list:
            return
        action = "install" if self.must_be_present else "uninstall -y "
        return [partial(package_action, action, " ".join(package_list))]


def is_installed(package_name: str):
    rc, _ = getstatusoutput(f"pip show {package_name}")
    return rc == 0


def package_action(action: str, package_list: str):
    rc = os.system(f"pip {action}  {package_list}")
    if rc != 0:
        raise Exception(f"Command terminated with non zero exit code {rc}")
