import os

import lxcraft


def test_debug():
    os.environ["DEBUG"] = "all"
    lxcraft.debug("test", "test")
