from setuptools import setup, find_packages

setup(
    name="QMatSim",
    version="0.1.0",
    description="Modular multiscale DFT + MD simulation framework",
    author="Meshal Alawein",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'qmatsim = qmatsim.__main__:main'
        ],
    },
    install_requires=[
        "numpy",
        "matplotlib",
        "pytest",   # Only if you want this included by default
    ],
)
