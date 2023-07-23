import os
from dataclasses import dataclass
from functools import partial
from subprocess import getstatusoutput


@dataclass
class PipPackages:
    """List of packages that must be installed"""

    package_list: list[str]

    def get_actions(self):
        package_list = []
        for package in self.package_list:
            if is_installed(package):
                continue
            package_list.append(package)
        if not package_list:
            return
        return [partial(package_action, " ".join(package_list))]


def is_installed(package_name: str):
    rc, _ = getstatusoutput(f"pip show {package_name}")
    return rc == 0


def package_action(package_list: str):
    rc = os.system(f"pip install {package_list}")
    if rc != 0:
        raise Exception(f"Command terminated with non zero exit code {rc}")
