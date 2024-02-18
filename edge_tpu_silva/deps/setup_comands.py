# edge_tpu_silva/deps/setup_commands.py
import subprocess
import os


def pi_setup_commands(sys: str = "Raspberry Pi"):
    try:
        print("\033[94mAttempting to install missing packages and hardware drivers from Coral\033[0m")
        # Additional commands from the .sh file
        commands = [
            'echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list',
            "curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -",
            "apt-get update",
            "apt-get install libedgetpu1-std",
            "python3 -m pip install --extra-index-url https://google-coral.github.io/py-repo/ pycoral~=2.0",
        ]

        for command in commands:
            try:
                # Try running the command without sudo
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError:
                # If command failed, try running with sudo
                os.system(f'sudo {command}')

        print(f"\033[92mSet up installation for {sys} completed.\033[0m")
    except:
        print(f"\033[91mSet up installation for {sys} failed to complete.\033[0m")

