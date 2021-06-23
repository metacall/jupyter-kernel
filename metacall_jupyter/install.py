import os
import argparse
import json
import sys

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

metacall_kernel_json = {
    "argv": [sys.executable, "-m", "metacall_jupyter", "-f", "{connection_file}"],
    "display_name": "metacall_jupyter",
    "language": "text",
}


def install_my_kernel_spec(user=True, prefix=None):
    """
    Installs the Kernel Specification

    Parameters:
        user: Checks the User installation
        prefix: Checks for the specific prefix
    """
    with TemporaryDirectory() as temporary_directory:
        # Starts off as 700; Not user-readable
        os.chmod(temporary_directory, 0o755)
        with open(os.path.join(temporary_directory, "kernel.json"), "w") as f:
            json.dump(metacall_kernel_json, f, sort_keys=True)
        print("Installing Jupyter Kernel for MetaCall Core")
        KernelSpecManager().install_kernel_spec(
            temporary_directory,
            "metacall_jupyter",
            user=user,
            prefix=prefix,
        )


def _is_root():
    """
    Checks if the User is an Admin on a UNIX platform
    """
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False


def main(argv=None):
    """
    Creates a function to pass Arguement Parser
    """
    parser = argparse.ArgumentParser(
        description="Kernel Installation for MetaCall Core"
    )
    prefix_locations = parser.add_mutually_exclusive_group()

    prefix_locations.add_argument(
        "--user",
        help="Install the KernelSpec in the User homedirectory",
        action="store_true",
    )
    prefix_locations.add_argument(
        "--sys-prefix",
        help="Install the KernelSpec in sys.prefix in a Virtual Environment",
        action="store_true",
        dest="sys_prefix",
    )
    prefix_locations.add_argument(
        "--prefix", help="Install the KernelSpec in the following prefix", default=None
    )

    args = parser.parse_args(argv)

    user = False
    prefix = None
    if args.sys_prefix:
        prefix = sys.prefix
    elif args.prefix:
        prefix = args.prefix
    elif args.user or not _is_root():
        user = True

    install_my_kernel_spec(user=user, prefix=prefix)

if __name__ == "__main__":
    main()
