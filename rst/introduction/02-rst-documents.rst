reStructuredText Documents
##########################

..  include::   /header.inc

My course notes are a collection of individual lectures, each a single **.rst**
file. The course is organized in sections, which are managed together ion a
directory named after the section topic. At the root of the course repository,
I place the sphinx_ configuration file and the top level **index.rst** file
containing the table of contents for the complete course. 

Rather than listing every lecture file title in the table of contents, I use
the sphinx_ **glob** feature that simply processes all files found in a
subdirectory. To get those files in something other than alphabetical order, I
name the lectures with leading two-digit numbers, so the files end up being
processed in the correct order. 

To get this project started, we need to build a piece of code that will do
something similar. 

Step 1: Set up the project
**************************

Like all good projects, we need to create a home for the project, and get it
under Git_ control. We also need to get it on GitHub_ so we have a safe "master"
copy in case our local development machine explodes! (Believe me, I have had
major failures using some unnamed vendor machines!)

Here is my start for this project:

..  code-block:: bash

    $ cd _projects
    $ mkdir -p rst_literate/{rst/_static,docs,src.tests}

Now, we can initialize the project so Git_ can manage it:

..  code-block:: bash

    $ cd rst_literate
    $ git init

We need a **.gitignore** file to keep cruft out of our remote repository:

..  literalinclude::    ../../.gitignore

Ideally, we add a **README.rst** to the project, so visitors to the project on
GitHub_ will see some information about the project. Here is a basic start on
this file:

..  literalinclude::    ../../README.rst

Now, we can get the project on github_. Assuming you have an account there,
create a new empty repository with the project name. I will show the required
commands using my GitHub_ user name, which is **rblack42**:

..  code-block:: bash

    $ git remote add origin https://github.com/rblack42/rst_literate.git
    



