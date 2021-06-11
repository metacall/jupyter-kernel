from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name = "metacall_jupyter",
    version = "0.1.0",
    description = "Wrapper Kernel for MetaCall Core Library leveraging IPython and Jupyter",
    long_description_content_type = "text/markdown",
    long_description = readme,
    license = "Apache-2.0",
    author = "Harsh Bardhan Mishra",
    author_email = "erbeusgriffincasper@gmail.com",
    url = "https://github.com/metacall/jupyter-kernel",
    install_requires = [
        "jupyter_client", "IPython", "ipykernel", "metacall"
    ],
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
)
