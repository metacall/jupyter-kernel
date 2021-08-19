.. MetaCall Jupyter Kernel documentation master file, created by
   sphinx-quickstart on Mon Jun 14 17:36:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MetaCall Jupyter Kernel's documentation!
===================================================

MetaCall Jupyter Kernel is an open-source wrapper kernel that implements
cross-language function calls through the `MetaCall Core`_ and the
`Polyglot REPL`_. MetaCall Core is an open-source library that brings
the polyglot programming experience to Developers. With MetaCall,
developers can embed different programming languages through an
easy-to-use high-level API.

The Kernel exposes the MetaCall Core API which can be loaded and
launched through a Jupyter Notebook interface. With this Notebook, the
users can try out writing, mixing and embedding code in different
programming languages.

When a `Jupyter`_ notebook of type ``metacall_kernel`` is opened, the
Kernel starts a new `Polyglot REPL`_ subprocess. In fact, the
``metacall_kernel`` makes the kernel behave like a wrapper over the
`Polyglot REPL`_ subprocess where standard input is imparted and the
standard output is fetched and displayed on the client interface.

To put it in a nutshell, ``metacall_kernel`` essentially comprises three
files which has to be installed:

-  **Kernel Spec**: `kernel.json`_
-  **Wrapper Kernel**: `kernel.py`_
-  **REPL subprocess**: `repl.js`_

Cell input in the Jupyter notebook is taken by `kernel.py`_ and sent via
`repl.js`_ to `Polyglot REPL`_ running through the subprocess. Output
from `Polyglot REPL`_ is collected by `repl.js`_ and given back to
`kernel.py`_ where it is analysed and transformed into an output format
that the `Jupyter`_ notebook understands, and thus eventually displayed.

.. _kernel.json: https://github.com/metacall/jupyter-kernel/blob/master/metacall_jupyter/install.py
.. _kernel.py: https://github.com/metacall/jupyter-kernel/blob/master/metacall_jupyter/kernel.py
.. _repl.js: https://github.com/metacall/jupyter-kernel/blob/master/repl.js
.. _Jupyter: https://jupyter.org/
.. _MetaCall Core: https://github.com/metacall/core
.. _Polyglot REPL: https://github.com/metacall/polyglot-repl

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   getting-started
   contributing
