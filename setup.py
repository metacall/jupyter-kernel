#!/usr/bin/env python3

#	MetaCall Jupyter Kernel by Parra Studios
#	A Jupyter Kernel for MetaCall.
#
#	Copyright (C) 2016 - 2021 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.

from setuptools import setup
import pathlib
import pkg_resources

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
        "Programming Language :: Python :: 3.6", #python is the default programming language
    ],
)
