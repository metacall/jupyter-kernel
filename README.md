# `MetaCall Jupyter Kernel`: Wrapper Kernel for MetaCall Core Library leveraging IPython and Jupyter

![Python CI build](https://github.com/metacall/jupyter-kernel/actions/workflows/ci.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/metacall/jupyter-kernel/master)
![Version 0.1.0](https://img.shields.io/badge/Version-0.1.0-brightgreen.svg)
![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

## Introduction

MetaCall Jupyter Kernel is an open-source wrapper kernel that implements cross-language function calls through the [MetaCall Core](https://github.com/metacall/core) and the [Polyglot REPL](https://github.com/metacall/polyglot-repl). MetaCall Core is an open-source library that brings the polyglot programming experience to Developers. With MetaCall, developers can embed different programming languages through an easy-to-use high-level API.

The Kernel exposes the MetaCall Core API which can be loaded and launched through a Jupyter Notebook interface. With this Notebook, the
users can try out writing, mixing and embedding code in different programming languages. The project is available on [PyPi](https://pypi.org/project/metacall-jupyter/).

## Key features

`metacall_jupyter` is designed to be simple and concise with the following key features:

- You can call functions in different programming languages, through cross-language function calls.
- You use a high-level API to execute code in different programming languages.
- Lists all the available functions and modules from the MetaCall's meta-object protocol.
- Official support for Python and NodeJS with the Polyglot REPL.
- Simple and intuitive user-experience centred around Polyglot development and components.

## Installation

It is recommended to use a Virtual Environment to manage your dependencies and the application build. We will first start with setting up the Local Project Environment:

```sh
git clone https://github.com/metacall/jupyter-kernel.git
virtualenv env
source env/bin/activate
```

Next we can download all the dependenices and setup the Kernel:

```sh
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 setup.py install
python3 -m metacall_jupyter.install
metacall npm install
```

Start your Jupyter Notebook by pushing the following command:

```sh
python3 -m metacall_jupyter.launcher
```

You can pick `metacall_jupyter` from the drop-down options and start working with the Jupyter Notebook interface. Example Notebook are found [here](examples).

## Docker

Build the image:

```sh
docker build -t metacall/jupyter .
```

Run the image:

```sh
docker run --rm --network=host -it metacall/jupyter
```

## Testing

To run the tests, push the following command:

```sh
pytest test-kernel.py
```

The script will run all the tests. To generate a coverage report, we are using the `pytest-cov` plugin, which can be invoked by pushing the following command:

```sh
pytest --cov=metacall_jupyter test-kernel.py
```

## Documentation

Our official documentation is available at [**metacall-jupyter-kernel.readthedocs.io**](https://metacall-jupyter-kernel.readthedocs.io/en/latest/index.html).

To edit the documentation you need a GitHub account. Once you have created one and logged in, you can edit any page by navigating to the corresponding file and clicking the edit (pen) icon. Alternatively create a fork, and then clone the repo and `cd` into the `docs` directory. Let us set the doucmentation up:

```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
make html
```

You can now open the documentation site on `_build/html/index.html` in your browser. Make corresponding changes on the documentation site and then run `make clean && make html` to update the documentation. You can now create a pull request to get your changes merged into the upstream branch.

## Contributing

To get started with contributing, check out the [Code of Conduct](CODE_OF_CONDUCT.md) and create an [Issue](https://github.com/metacall/jupyter-kernel/issues/new) to get started.

If you are new to Git & GitHub, you can find more information [here](https://metacall-jupyter-kernel.readthedocs.io/en/latest/contributing.html). It contains all the information about making the changes, linting, running the CI locally and submitting the pull request.

You can view the [Change Log](CHANGELOG.md) to see what has changed in the project, since its inception.

## LICENSE

[Apache-2.0 License](LICENSE)
