from setuptools import setup, find_packages

setup(
    name="pip-example",  # Replace with your project name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",  # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "run-app=app:main",  # Replace with your entry point function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
