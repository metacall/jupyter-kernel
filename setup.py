from setuptools import setup
import pathlib
import pkg_resources
import setuptools


with open("README.md", "r") as f:
    readme = f.read()

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="metacall_jupyter",
    version="0.1.0",
    description="Wrapper Kernel for MetaCall Core Library leveraging IPython and Jupyter",
    long_description_content_type="text/markdown",
    long_description=readme,
    license="Apache-2.0",
    author="Harsh Bardhan Mishra",
    author_email="erbeusgriffincasper@gmail.com",
    url="https://github.com/metacall/jupyter-kernel",
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
)
