# Development of Jupyter Kernel for MetaCall Core

![image](assets/project-banner.gif)

![Python CI build](https://github.com/metacall/jupyter-kernel/actions/workflows/ci.yml/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Introduction

This project aims to create a kernel where the MetaCall Core can be loaded and launched through a Jupyter Notebook interface. With this Notebook, the users can try out writing and embedding code in different programming languages.

It would also make it possible to use the MetaCall API and achieve the goal of bringing a unified interface for developers to try out and leverage MetaCall. The Kernel would allow developers to load the MetaCall API to execute code in different programming languages by mixing code amongst each other.

Check out the [Google Summer of Code Project](https://summerofcode.withgoogle.com/projects/#5883852846792704) to be developed by [Harsh Bardhan Mishra](github.com/harshcasper) under the mentorship of [Gil Arasa Verge](github.com/giarve).

## Installation

It is recommended to use a Virtual Environment to manage your dependenices and the application build. We will first start with setting up the Local Project Environment:

```sh
git clone https://github.com/metacall/jupyter-kernel.git
virtualenv env
source env/bin/activate
```

Next we can download all the dependenices and setup the Kernel:

```sh
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 setup.py install
python3 -m metacall_jupyter.install
```

Start your Jupyter Notebook by pushing the following command:

```sh
python3 -m metacall_jupyter.launcher
```

You can pick `metacall_jupyter` from the drop-down options and start working with the Jupyter Notebook interface. An example notebook showing the execution of Node Scripts can be found [here](examples).

## Docker

Build the image:
```sh
docker build -t metacall/jupyter .
```

Run the image:
```sh
docker run --rm --network=host -it metacall/jupyter
```

## Contributing

To get started with contributing, check out the [Code of Conduct](CODE_OF_CONDUCT.md) and create an [Issue](https://github.com/metacall/jupyter-kernel/issues/new) to get started.

## LICENSE

[Apache-2.0 License](LICENSE)
