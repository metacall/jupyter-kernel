Getting Started
===========

Starting a notebook
-------------------

To start a notebook, type in a terminal:

::

   jupyter notebook

Your default webbrowser should open with a list of the files in the
current directory. Choose ``New->metacall_kernel`` to open a new
notebook of type ``metacall_kernel``.

You can also start a nootbook directly from the commandline using our
launcher script:

::

   python3 -m metacall_jupyter.launcher

Closing a notebook
------------------

To close the notebook, choose:

::

   File -> Close and Halt

from the menu.

Note that simply closing the browser tab does not close the notebook or
the running MetaCall Polyglot REPL subprocess(es) behind it. You can
reopen the tab by clicking on the name of your notebook (next to the
then green icon).

It is also possible to kill the MetaCall REPL subprocess(es) running
behind the notebook by clicking on the Shutdown button in the running
notebook section of your Jupyter session.

You can optionally use the programmatic way to shutdown by pushing it in
the cell and executing it:

::

   $shutdown

It will gracefully kill the running subprocess and you can safely exit
from the notebook.

Running a notebook
------------------

MetaCall Jupyter kernel supports a few commands that allows you to
interact with the MetaCall Polyglot REPL to load and execute code in
different languages. The other commands and magics allow you to load
foreign functions on the language, interact with the shell and inspect
the meta-object protocol.

You can check-out all the available functionalities using the ``$help``
command on the cell and execute it. You will get the following output:

::

   1. ! : Run a Shell Command on the MetaCall Jupyter Kernel
   2. $shutdown : Shutdown the MetaCall Jupyter Kernel
   3. $inspect : Inspects the MetaCall to check all loaded functions
   4. $loadfile: Loads a file onto the MetaCall which can be evaluated
   5. $newfile: Creates a new file and appends the code mentioned below
   6. %repl <tag>: Switch from different REPL (available tags: node, py)
   7. >lang: Execute scripts using the MetaCall exec by saving them in a temporary file (available languages: python, javascript)
   8. $loadcell <tag>: Loads a function onto the MetaCall to be evaluated
   9. $help: Check all the commands and tags you can use while accessing the MetaCall Kernel
   10. $available: Checks all the available REPLs on the Kernel

You can load a REPL, by just passing ``%repl <tag>`` where you can
replace ``<tag>`` with the languages available. You can check-out the
available languages through the ``$available`` command.

Exporting the notebook
----------------------

You can export a reproducible copy of the Notebook by choosing:

::

   File -> Download as

You can download the Notebook in a Notebook (``.ipynb``), PDF, HTML,
Markdown and more formats easily. Make sure to save and checkpoint to
ensure a reproducible copy on your own local machine:

::

   File -> Save and Checkpoint