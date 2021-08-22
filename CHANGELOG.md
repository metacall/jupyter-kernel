# Change Log

## 0.1.0

Released on August 22, 2021.

### Added

First version of the MetaCall Jupyter kernel that follows the wrapper kernel mechanism using IPython and the Jupyter client:

- Setup the wrapper kernel using IPython and the Jupyter client.
- Integrated the Polyglot REPL into the Jupyter client and added support for Python & NodeJS.
- Added user-experience features for the kernel such as `$loadfile`, `$loadcell`, `$inspect` to load foreign modules and implement cross-language function calls. More information [here](https://metacall-jupyter-kernel.readthedocs.io/en/latest/getting-started.html#running-a-notebook).
- Added support to run Shell commands from the kernel.
- Implemented the CI/CD pipelines for the project using GitHub Actions.
- Containerized the project using [Docker](https://www.docker.com/).
- Implemented the tests for the project using PyTest.
- Developed the documentation using Sphinx, published on ReadTheDocs [here](https://metacall-jupyter-kernel.readthedocs.io/en/latest/).
