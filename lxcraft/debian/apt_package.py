from dataclasses import dataclass
from subprocess import getstatusoutput

import lxcraft


@dataclass
class AptPackages(lxcraft.Resource):
    """List of packages that must be installed"""

    package_list: list[str]

    def create(self):
        package_list = " ".join(self.package_list)
        lxcraft.system(f"apt install -y {package_list}")

    def destroy(self):
        package_list = " ".join(self.package_list)
        lxcraft.system(f"apt remove -y {package_list}")

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
        command = (
            "dpkg-query --showformat '${Status}'"
            f" --show {package_name} | grep -q '^install ok installed$'"
        )
        rc, _ = getstatusoutput(command)
        lxcraft.debug("command", command, f"# rc={rc}")
        return rc == 0
