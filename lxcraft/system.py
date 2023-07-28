import os

from taglogger import tlog


def system(*args, ignore_errors=False, **kwargs):
    """Run a shell command"""
    rc = os.system(*args, **kwargs)
    tlog(
        "command",
        *args,
        **kwargs,
    )
    tlog("command", f"# rc={rc}, ignore_errors={ignore_errors}")
    if not ignore_errors and rc != 0:
        raise Exception(f"Command terminated with non zero exit code {rc}")


# def get_output(*args, **kwargs):
#     """Run a shell command"""
#     rc, output = subprocess.getstatusoutput(*args, **kwargs)
#     tlog(
#         "command",
#         *args,
#         f"# rc= {rc}",
#         **kwargs,
#     )
#     if rc != 0:
#         raise Exception(f"Command terminated with non zero exit code {rc}")
#     return output
