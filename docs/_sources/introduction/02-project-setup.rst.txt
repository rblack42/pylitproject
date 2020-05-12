Starting a Python project
#########################

..  include::   /header.inc

Most students begin a project by writing code. That is definitely not how we
start a significant project. We have some setup work to do first:

But forst, we have to get this project started.

Step 1: Set up the project
**************************

Like all good projects, we need to create a home for the project, and get it
under Git_ control. We also need to get it on GitHub_ so we have a safe
"master" copy in case our local development machine explodes! (Believe me, I
have had major failures using some unnamed vendor machines!)

Here is my start for this project:

Project Directory
=================

First, we create a top-level directory for the project. I keep all active
development projects under **_projects** in my home directory:

   ..  code-block:: bash

    $ cd _projects
    $ mkdir pylitproject

For the rest of the setup, we need to be working in this new directory;

..  code-block:: bash

    $ cd pylitproject

We will be doing a lot of documenting in this project. I keep all |RST| files
under **rst**. Using Sphinx_ (for now), we will process the **.rst** files into
**html** files, placing them in a second file named **docs**. By doing this we
get a free website where we can publish our documentation on Github_. We need
one magic file in the **docs** folder to get the website working properly;

..  code-block:: bash

    $ mkdir -p rst/_static
    $ mkdir -p docs
    $ touch docs/.nojekyll

This project will be hosted on PyPi_, so users can install it using **pip**.
The project code will be placed in a Python package with the same name as the
project:

..  code-block:: bash

    $ mkdir -p pylitproject
    $ touch pylitproject/__init__.py

Finally, we will be testing the code as we proceed with development. All test
files will be placed in a **tests** package directory:

..  code-block:: bash

    $ mkdir -p tests
    $ touch tests/__init__.py

Step 2: Manage with Git
***********************

Now, we can initialize the project so Git_ can manage it, Make sure that this
command is run in the top-level project directory:

..  code-block:: bash

    $ git init

We need a **.gitignore** file in the top-level project directory to keep cruft
out of our remote repository:

..  literalinclude::    ../../.gitignore
    :caption: .gitignore

If you are going to use Github_ as a home for your project, you need a
top-level **README.rst** file, so visitors to the project on GitHub_ will see
some information about the project. Here is a basic start on this file:

..  literalinclude::    ../../README.rst
   :caption:    README.rst

Step 3: Create a Github Repository
**********************************

Now, we can get the project on Github_. Assuming you have an account there,
sign in and create a new empty repository with the project name. Once you get
that done, return to your development machine and run a few final commands:

..  code-block:: bash

    $ git remote add origin https://github.com/rblack42/rst_literate.git

..  note::

    This example includes my Github_ username, which is **rblack42**.
    Obviously, you should use your own username here.

Finally, we "push" everything (except things we told Git_ to ignore in the
**.gitignore** file) to Github_.

..  code-block::    bash

    $ git add .
    $ git commit -m "initial project commit"
    $ git push -u origin master

There is a pattern in this set up commands that we will follow over and over as
we work on this project.

The first line tells Git_ to scan the entire project directory and
subdirectories, looking for any changes made since the last time we "committed"
changes to the project. Since we are just starting, this "add" command will add
all files and directories to the Git_ management system stored in a hidden
**.git** folder in your project directory.

You "commit" those changes with the second command line above. This step wraps
us all of the changes and marks this version of your project code with a unique
40 character tag. Git_ can return your project directory to this version later
if needed. Most of the time we do not worry about this tag, we can add human
readable tags later.

Finally, the last command line above actually does copy your new version to
Github_.

..  warning::

    The **-u** option is only added to this command the first time you push
    your project to Github_. Leave it off after that.

Step 4: Add Documentation
*************************

In order to use Sphinx_ to document this project, we need to do a bit more
work.

First, we need to add a configuration file to the **rst** directory:

..  literalinclude::    /conf.py
    :caption:   rst/conf.py

Only a few lines in this file change from project to project. Details will be
explained later.

We also need a top-level |RST| page, named **index.rst** which will be the
entry point to our documentation.

..  literalinclude::    /index.rst
    :caption: rst/index.rst

Notice that I am using the Sphinx_ **glob** feature to include documentation
files under an **introduction** subdirectory. (The file you are reading now is
in that directory).

Run Sphinx_ at lease once (using the **makefile** shown below), so you have web
pages in the **docs** directory. Then, sign on to your Github_ account and go yo
your project repository page. Under the **settings** menu item, scroll down
until you see *Github Pages*. Change the *source* selection that says **None**
to *Master branch/docs folder*. Finally, push your new web pages to Github_
using the three step *mantra* we showed earlier. You should see those pages in
any web browser by navigating to a URL like this:

    * https://rblack42.github.io/pylitproject

Again, use your own Github_ account name here.

Step 5: Project Dependencies
****************************

Hardly any significant Python project is totally self-contained. Most projects "depend"
on tools written by other developers. Those tools are loaded onto your system
using **pip**. It is traditional to list all of these "dependencies" in a
**requirements.txt** file in your project"

..  literalinclude::    ../../requirements.txt
    :caption: requirements.txt

Step 6: Project Makefile
*************************

We will be doing a lot of different tasks in our development work. The
individual commands needed for each task can be hard to remember. Therefore, we
will write down all of those commands in a project **Makefile**, and use Make_
to run them for us, using a simple, easy to remember command. (See the Appendix
for more on this file and the Make_ command):

..  literalinclude::    ../../Makefile
    :caption: Makefile

Step 7: Testing!
****************

As we write code, we will test things. We will be using *Test Driven
Development* in this project, which means we will write some test code for any
new feature we add, then write the code needed to make sure that test "passes".
We will use a Make_ command to run tests locally, but there is a neat way we
can run tests on a variety of machines, all for free. We will use Travis-CI_
which will run our tests for us on a remote system set up as we wish every time
we push changes on Github_.

To set this up, we need a control file in our project:

..  literalinclude::    ../../.travis.yml
    :caption: .travis.yml

We will go over this file later.

Once you have this file in place, sign in to Travis-CI_ (you can use your
Github_ credentials to do this), and look for your project under the account
settings menu item. You need to toggle testing on for this project in the list
of repositories shown.  Once that is done, simply "push" changes to Github_ and
Travis-CI_ will see those changes, 'clone' a fresh copy of your project into a
new virtual machine, and run the tests you specified. If everything works, you
will see the results in the badge we included on the **REAdme.rst** file. Check
your project page on Github_ to see this.

That is enough setup work for now, let's start working on code!
