import os

import lxcraft


def system(*args, **kwargs):
    """Run a shell command"""
    rc = os.system(*args, **kwargs)
    lxcraft.debug("command", rc, *args, **kwargs)
    if rc != 0:
        raise Exception(f"Command terminated with non zero exit code {rc}")
