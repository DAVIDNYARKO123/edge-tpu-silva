import re
from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of README.md from the parent directory
readme_path = Path(__file__).parent.parent.parent / "README.md"
with open(readme_path, "r", encoding="utf-8") as readme_file:
    readme_content = readme_file.read()

# Remove image-related HTML tags using regular expressions
image_regex = re.compile(r"<img[^>]*>")
filtered_long_description = re.sub(image_regex, "", readme_content)

setup(
    name="edge_tpu_silva",
    version="1.0.4",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "ultralytics",
    ],
    entry_points={
        "console_scripts": [
            "silvatpu = edge_tpu_silva.__main__:silvatpu",
            "silvatpu-sys = edge_tpu_silva.deps.check:setup_message",
            "silvatpu-linux-setup = edge_tpu_silva.deps.setup_comands:linux_setup_commands",
        ],
    },
    long_description=filtered_long_description,
    long_description_content_type="text/markdown",
)
