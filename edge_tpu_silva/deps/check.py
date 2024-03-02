import platform

import pkg_resources


def get_platform():
    system = platform.system()
    if system == "Linux":
        return "Linux/Debian"
    elif system == "Darwin":
        return "Mac OS"
    elif system == "Windows":
        return "Windows"
    else:
        return "Unknown"


def get_installed_version(package_name):
    try:
        return f"{package_name} {pkg_resources.get_distribution(package_name).version}"
    except pkg_resources.DistributionNotFound:
        return None


def setup_message():
    current_platform = get_platform()
    edge_tpu_silva_version = get_installed_version("edge-tpu-silva")
    linux_entry_point_name = (
        "\033[94msilvatpu-linux-setup\033[0m"  # Blue color ANSI escape code
    )

    if current_platform == "Linux/Debian":
        message = (
            f"You are on a {current_platform} system. To complete the setup for installation of edge-tpu-silva.\n\n"
            f"    run: {linux_entry_point_name}\n"
        )
        print(f"\033[92m{message}\033[0m")  # Green color ANSI escape code
    else:
        error_message = (
            f"You are on {current_platform} system. {edge_tpu_silva_version} is not supported on your platform. \n\nVisit Coral for specific installation steps for (Coral and Pycoral) for your platform:\n"
            f"    \033[94mhttps://coral.ai/\033[0m"
        )
        print(f"\033[91m{error_message}\033[0m")  # Red color ANSI escape code
