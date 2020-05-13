pylitproject: (v0.0.3-dev)
##########################
:Author: Roie R. Black
:Date: May 7, 2020
:Email: roie.black@gmail.com
:Documentation: https://rblack42.github.io/pylitproject

|travis-build| |license|

This is the *PyLiT Project*, a project designed to build an efficient tool that
incorporates Dr. Donald Knuth's basic ideas for Literate Programming into a
documentation build system suitable for educational use by instructors.

Instead of generating documenting for just one version of a program, this tool
allows the developer to build a document that follows along as the project
evolves. In order to make that happen, extensions to Knuth's Literate
Programming markup are added so code can be modified to produce a new version.

Code extracted from the documentation is styled according to the developer's
tastes, and not obfuscated as Knuth originally wanted. Hopefully, this will
encourage use by developers who like to read their code directly.

The documentation files are managed in a block-structured store similar to that
used by git. This speeds up processing by eliminating builds on files already
processed and unchanged.

..  note::

    At the present time, the documentation is managed by Git, not the extracted
    code. That means that developers interested in a project managed by PyLiT
    will need to "read the documentation", not the bare code. (Is that really a
    bad thing?) I welcome ideas on how to manage extracted code in the
    traditional form so it can be stored and viewed on Github.

..  |travis-build| image:: https://travis-ci.org/rblack42/pylitproject.svg?branch=master
    :alt: Build badge from Travis-CI

..  |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :alt: BSD 3-Clause License



