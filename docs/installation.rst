Installation
-------------------

When you have the MetaCall’s Jupyter Kernel repository cloned and set
up, you are ready to install the software and tools you will use to
modify the kernel and push your changes.

What you require?
~~~~~~~~~~~~~~~~~

-  A bash shell environment (Linux and OS X include a bash shell
   environment out of the box, but if you are on Windows you can use
   Cygwin)
-  Python 3.x
-  Git
-  NodeJS
-  A web browser (Firefox, Chrome, or Safari)
-  Docker

.. _Vincent Driessen’s Git Branching: https://nvie.com/posts/a-successful-git-branching-model/
.. _sign up for a GitHub account: https://www.github.com/join
.. _generate and set up SSH keys on GitHub: https://help.github.com/articles/generating-ssh-keys/

Install the required software dependencies on a Linux system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is recommended to use a Virtual Environment to manage your
dependenices and the application build. We will first start with setting
up the Local Project Environment:

::

   virtualenv env
   source env/bin/activate

Next we can download all the dependenices and setup the Kernel:

::

   curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
   python3 -m pip install --upgrade pip
   pip3 install -r requirements.txt
   python3 setup.py install
   python3 -m metacall_jupyter.install
   metacall npm install

Start your Jupyter Notebook by pushing the following command:

::

   python3 -m metacall_jupyter.launcher

You can pick ``metacall_jupyter`` from the drop-down options and start
working with the Jupyter Notebook interface.

Building the Kernel
~~~~~~~~~~~~~~~~~~~

With the initial setup complete, you are ready to make changes to the
kernel. From the ``metacall_kernel`` directory, once you have made your
changes, run through your changes:

::

   python3 -m metacall_jupyter.install
   python3 -m metacall_jupyter.launcher

Docker setup
~~~~~~~~~~~~~

Build the image:

::

   docker build -t metacall/jupyter .

Run the image:

::

   docker run --rm --network=host -it metacall/jupyter

Run the Tests
~~~~~~~~~~~~~

To run the tests, push the following command:

::

   pytest test-kernel.py

The script will run all the tests. To generate a coverage report, we are
using the pytest-cov plugin, which can be invoked by pushing the
following command:

::

   pytest --cov=metacall_jupyter test-kernel.py

Set up the documentation
~~~~~~~~~~~~~~~~~~~~~~~~

To setup the Sphinx documentation on your local machine, enter into the
``docs`` directory and install all the local dependenices:

::

   cd docs
   pip3 install -r requirements.txt

You can now build your documentation’s static html assets with sphinx
using ``make``:

::

   make html

After making the changes, you will be able to rebuild your
documentation’s html:

::

   make clean && make html

Code Formatting
~~~~~~~~~~~~~~~

We use PyLint and Flake8 for code linting and Black for code formatting.
Flake8 is used in our Continuous Integration pipeline on GitHub, and
hence we would like to see zero Flake8 issues before code merge. To
verify the issues raised by Flake8, just run:

::

   flake8

To run Black against the source directory or a particular file you have
edited, run:

::

   black <SOURCE_DIRECTORY_OR_FILE>
