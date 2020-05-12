Literate Programming and reStructuredText
#########################################

..  include::   /header.inc

I have been using |RST|_ for almost since it was first released by David
Goodger in 2003. I moved to Python Sphinx_ shortly after it was released by
Georg Brandl in 2008. I used these tools to process thousands of pages of
lecture notes for Computer Science courses I taught at |ACC|_ in Austin Texas.

Overall, I was mostly satisfied with the result. I hosted my lectures on a
virtual private server, freely available to anyone wishing to explore the courses, and
even had a few students across the globe follow along in a course. I used several
extensions developed by others and myself to enhance my notes. However, in the
end, there was still something missing.

Lecture Notes
*************

My lectures always tell a story. They are not just a presentation of dry facts.
I have always tried to take students on a journey of discovery. Along the way,
I introduce them to the tools of their trade, to prepare then for whatever job
waits for them. That means I present code examples that start off small and
build up to a complete final program.  I run these code examples as I discuss
them in the notes. A single small program may go through several evolutionary
steps until it reaches an end point. If you think about it, a set of lectures
presenting a single program from start to finish is the kind of documentation
maintainers need. They are designed to take the reader on the journey of
development, explaining everything along the way! In a classroom setting the
"why" of the code is very important!


How did I make all of that happen using Sphinx?

The answer is a bit painful, I ended up maintaining many different versions of
the example code and included those versions in the notes. For static display of these
examples, that is fine. I used a Sphinx extension to run those different
versions and capture the output in the notes as well.

The problem is that maintaining all of those versions is a bit of a mess, and
is not a sane way to manage any project, even an educational one.

Enter Git
=========

Most modern software development involves a source-code-control system of some
sort. Since it is hugely popular these days, I introduce my students to Git_,
which can maintain the history of an evolving project without much work on the
users part. Why am I maintaining all of those intermediate versions of
something when Git_ can do all of that?

Unfortunately, getting Git_ and Sphinx_ to play nicely together is not easy.

In order to  retrieve old versions of my example code I need to run a **git
checkout** command. Unfortunately, I need to do that as Sphinx_ is processing
pages. Since the entire class is normally under Git_ control, that would change
all of the code in the local working copy to the version that existed when that
code example was created. That just does not sound like a good idea!

Instead I kept examples in a separate repository managed by custom extensions
to Sphinx as it processed my lecture notes. That worked, but now I had two
repositories to manage for each course, and including code from a different
repository into the lecture notes was not a simple solution. I had to run back
and forth between repositories to manage all of the notes.

Literate Programming
====================

Back around 1984, Dr. Donald Knuth unveiled something he called *Literate
Programming*. His idea was to embed code fragments, much like those I include
in my lecture notes, directly in a document designed for human readers. (Boy,
that sounds exactly like my lecture notes!) Dr. Knuth created tools that
extracted all of those code fragments, and stitched them together in a
human-unreadable form for processing by conventional tools like compilers. Dr.
Knuth wanted developers to explain their code to other humans and never worry
about the code files the compiler actually saw. This would produce
documentation much better suited to the long term needs of a significant
project!

But Dr. Knuth's idea never really took off, and I am sure that was a bit
disappointing to him. I read his original paper on this idea while teaching at
the |AFIT|, the USAF graduate school in Dayton, Ohio, and immediately saw an
application for this idea in the classroom. I had often puzzled over why
students put project code together the way it ended up being submitted. If I
had proper tools for them to explain their *thinking* as the constructed their
code, it would be far easier to spot bad habits, and re-aim those students in
better directions.

Sadly, I never followed through on that idea, but it lingered in my mind
throughout my Air Force career, and later through my teaching career at |ACC|_.

Part of why *Literate Programmng* failed to take off, at least in my mind, is
that programmers were not willing not give up looking at their "well written"
code, and having that code managed by good source-code-control systems. They
work hard to get the code clean and easy to follow. In far too many cases, that
code is all maintainers have to go by when they need to dig into that project
code.  Documentation, especially documentation that explains the *why* of the
code is largely missing.

..  note::

    Do NOT get me started on any project where the developer explains a lack of
    proper documentation by stating: "Read the code'!

Using |LP| in my lecture notes seemed like something nice to do, but it has
another problem. I am not explaining one large program, I am explaining several
programs, and versions of those program as they evolve. All that code changes
as i tell my story in a class!  Features are added, removed, and moved around.
That makes using the standard tools of |LP| inadequate for the task without
some work.

Non-Linear Flow
***************

|LP|_ envisioned nice books (or at least PDF files) of documentation for a
project. Knuth, himself, used his tools to document the TeX_ project, and
others, and those books sit proudly on my book self!

A book is usually a linear thing, designed to be read from page one to the end.
Yes, it is possible to generate a book designed so that individual sections can
be read in any order, but the key idea, I think, in |LP| is to give the
developer a way to explain the flow of the project, the decisions made, and
maybe even the mistakes made along the way. Really good documentation details
the "why" of the code, not just the "what" of that code.

The story to be told is a linear one, but the development of the code was
definitely not linear!

..  note::

    I used to tell my graduate students, when they started writing their
    thesis, to pretend you knew where you were going all the way from start to
    finish. They could leave out the missteps and false ideas that they tried
    and abandoned. In looking back, maybe capturing some of that would be
    helpful, but it did keep the thesis focused on the result produced, which
    was wat most advisory committees wahted to discuss!

Developers usually build their code in one of two ways: top-down or bottom up.
In top-down, they focus on the high level aspects of the project, and move
toward details later.

In bottom-up they build small parts that are combined to build bigger constructs.
Ultimately, you reach the top and the entire project is done.

Yes, it is possible to combine both of these approaches and build in a hybrid
way.  No matter how we evolve the documentation, ultimately we need to invoke a
tool to produce the required format, mostly html, or pdf in my case.

Sphinx_ starts off by processing the files in the order indicated by the table
of contents. However, later runs may skip files and process them in a somewhat
random order. The output of the run is a collection of HTML pages, or a single
file to be processed by LateX_ into a final PDF file. I need to extract code
along the way, as the story unfolds. I need a way to
build versions of the code and run them, then modify that code for a later
run. Sounds hard to manage, but this is exactly how developers move their
projects through the development process.


Don't Repeat Yourself!
**********************

There is one more important observation I want o make here.

Programmers are taught not to repeat themselves (*DRY*) athis "law" usually
means factoring out common code into a function, but in the end we repeat
ourselves all the time, and never give it a single thought.

When I process lecture notes with Sphinx_ or process source code files with a
compiler, there is a lot of repeating going on!.

Why?

The reason is simple, we never save any intermediate results of earlier
processing in a meaningful way. If we did that, we might avoid much of the work
going on as we repeatedly build products! At least with processing my |RST|
files, I have an idea for a better way, but that means ditching SPhinx_ and
starting over:

Here is a quote I like:

::
    ".. plan to throw one away; you will, anyhow."

    Fred Brooks | The Mythical Man-Month

That leads me to the current project. I want to build a tool that will produce
high-quality documentation (or lecture notes) showing how code is developed,
and show how to manage that code, test that code, and run that code along the
way. I also want to apply the *DRY* principle as much as I can as this tool evolves.

Sounds simple enough!

Let's get started!

