Contributing
============

Bug fixes, performance improvements, code formatting. There are a lot
ways in which you can contribute! The issues list of a project is a
great place to find something that you can help us with.

To increase the chances of your contribution getting merged, please
ensure that:

-  You satisfy our code of conduct.
-  Your code follows our coding guidelines.
-  Your submission follows Vincent Driessen’s Git Branching System.
-  Your pull request:

   -  Passes all checks and has no conflicts.
   -  Has a well-written title and message that briefly explains your
      proposed changes.

We welcome all kinds of bug reports, user feedback and feature requests!
To get started with contributing for the very first time on GitHub, we
have a few steps outlined for you.

Create a GitHub account
-----------------------

Before you can contribute to MetaCall’s Jupyter Kernel, you must sign up
for a GitHub account.

Set up authentication
---------------------

When you have your account set up, follow the instructions to generate
and set up SSH keys on GitHub for proper authentication between your
workstation and GitHub.

Confirm authentication is working correctly with the following command:

::

   ssh -T git@github.com

Fork and clone the repository
-----------------------------

You must fork and set up the MetaCall’s Jupyter Kernel repository on
your workstation so that you can create PRs and contribute. These steps
must only be performed during initial setup.

1. Fork the https://github.com/metacall/jupyter-kernel repository into
   your GitHub account from the GitHub UI. You can do this by clicking
   on **Fork** in the upper right-hand corner.
2. In the terminal on your workstation, change into the directory where
   you want to clone the forked repository.
3. Clone the forked repository onto your workstation with the following
   command, replacing with your actual GitHub username:
   ``git clone git@github.com:<user_name>/jupyter-kernel.git``
4. Change into the directory for the local repository you just cloned.
   ``cd jupyter-kernel``
5. Add an upstream pointer back to the MetaCall’s remote repository, in
   this case ``jupyter-kernel``.
   ``git remote add upstream git@github.com:metacall/jupyter-kernel.git``
   This ensures that you are tracking the remote repository to keep your
   local repository in sync with it.

Making the changes
------------------

Follow the install instructions to setup the project locally. After you
are done making the changes, make sure to run Black and Flake8 for code
linting and formatting respectively. We have a pre-configured Flake8
configuration and once you run ``black`` against the source directory or
file, run Flake8 to verify that linting checks pass:

::

   flake8

Optionally, we would also like the Continous Integration to pass
successfully and would advise for the usage of ``act`` for running the
workflows locally. ``act`` is a tool offered by Nektos which provides a
handy way to run GitHub Actions locally using Docker.

``act`` can be set up locally with Homebrew, Chocolatey or even a simple
BASH script. To set it up using the BASH script, just push the following
command on your terminal:

::

   curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

Next step is to define the custom image that we can use to run our
actions locally. ``act`` provides a micro, medium and larger Docker
image for Ubuntu GitHub runner. ``act`` does not support Windows and
macOS images yet.

While running ``act`` for the first time, we can define the image that
we would like to utilize for our local CI runs. The configuration is
saved inside the ``~/.actrc`` file.

In the cloned repository, while running ``act`` for the first time, it
will find the ``./.github/workflows`` and all the workflows present. To
checkout the jobs listed as part of the GitHub Actions CI, push the
following command:

::

   act -l

It will list all the jobs and you can pick up the particular jobs you
wish to run. If you are looking to run a particular job, push in the
following command:

::

   act -j <JOB_NAME>

To run the job in dry run, push in the following command:

::

   act -n

To run the job with verbose logging, push in the following command:

::

   act -v

To reuse the containers in ``act`` to maintain state, push in the
following command:

::

   act -j <JOB_NAME> --bind --reuse

If the workflow is running successfully, you can now be confident about
your changes and be ready to send a Pull Request for the same.

Sending a Pull Request
----------------------

When your work is ready and complies with the project conventions,
upload your changes to your fork, by making a clean commit. Make sure
that the changes being proposed are from a branch and not the
``master``.

::

   git push -u origin Branch_Name

Go to your repository on your browser and click on **Compare** and pull
requests. Add a title and description to your pull request that explains
your contribution. Voila! Your Pull Request has been submitted and will
be reviewed by the maintainers and merged.

.. _here: https://github.com/metacall/jupyter-kernel/blob/master/examples
