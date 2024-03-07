# edge_tpu_silva/deps/setup_commands.py
import os
import subprocess

import argparse
from .check import get_platform

def libedgetpu(option):
    if option == 'max':
        package_name = 'libedgetpu1-max'
    else:
        package_name = 'libedgetpu1-std'

    return package_name

def linux_setup_commands(sys: str = "Linux/Debian"):
    parser = argparse.ArgumentParser(description='Install libedgetpu package.')
    parser.add_argument('--speed', choices=['std', 'max'], default='std', help='Choose between libedgetpu1-std or libedgetpu1-max')
    args = parser.parse_args()
    opt = libedgetpu(args.speed)

    platform = get_platform()

    if platform == sys:
        try:
            print(
                "\033[94mAttempting to install missing packages and hardware drivers from Coral\033[0m"
            )
            # Additional commands from the .sh file
            commands = [
                'echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list',
                "curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -",
                "apt-get update",
                f"apt-get install {opt}",
                "python3 -m pip install --extra-index-url https://google-coral.github.io/py-repo/ pycoral~=2.0",
            ]

            for command in commands:
                try:
                    # Try running the command without sudo
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError:
                    # If command failed, try running with sudo
                    os.system(f"sudo {command}")

            print(f"\033[92mSet up installation for {sys} completed.\033[0m")
        except:
            print(f"\033[91mSet up installation for {sys} failed to complete.\033[0m")
    else:
        error_message = (
            "ERROR: You are not on a Linux/Debian platform. The setup command you "
            "just used is for only Linux/Debian platforms."
        )
        print(f"\033[91m{error_message}\033[0m")  # Red color ANSI escape code
