from setuptools import setup, find_packages


setup(
    name="edge_tpu_silva",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
    ],
    entry_points={
        "console_scripts": [
            "silvatpu = edge_tpu_silva:silvatpu",
            "setup-pi-tpu = edge_tpu_silva.deps.setup_comands:pi_setup_commands",
        ],
    },
)
