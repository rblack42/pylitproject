Sphinx LP Directive
###################

..	include::	/header.inc

To get Sphinx to process |LP| blocks, we need a new directive. For simplicity,
this directive will be named **pylit** and have this structure::

	* The argument on the directive line will identify the language used by the block

	* The **caption** option will name the block

		** Caption text must be formed formally (see below)

	* Lines can be numbered using **linenos**

The **caption** line must be formed as follows:

    :caption:   <type>: caption text

Where <type> is one of four basic |LP| block types:

	* **file** - marks the beginning of a file. The caption provides the path

	* **code** - marks the start of a named block of code. The caption provides the name

    * **add** - extends either an existing **file** or **code** block list,
      adding this block to the end of the list

    * **shell** - content is a set of shell commands to be executed. The code
      existing in the build directory may be run, but that code may change later
      in the document. The output will be placed in the text below the command
      list

..	note::

    If either a **file** or a **code** block is repeated in the text, the
    original named block list is discarded and a new one started. Subsequent
    references to these names will expand with the new content/

Cross Referencing Blocks
************************

ALl blocks in a document are numbered sequentially, beginning at the root of the document. When a block is referenced in another block, that reference is used to create a cross reference in the final output. Following Knuth's examples, when you define any named block, we create a link point to that place in the document. When that named block is used, we ceate a list of "used in" references at the end of the first defining block. At the end of the document, we can creqate a full list of named blocks, together with a cross reference list showing where that block was used.

References to a named block are included in code using special comments that look like this:

    * #<<block name>>

The notation chosen depends on the line comment marker for the chosen language. If the block has not been defined, the include marker will remain in the expanded code as a comment.

..  todo::

    Consider changing **pylit** to a domain name, and make the directive refer
    to the block kind. Captions would become just the label needed to identify
    the block list.

..  todo::

    We need additional directives to generate a list of blocks, similar to a list of figures.

..  todo::

    Code blocks should be numbered and cross referenced in the document. Only
    the root block in a list needs this number, (Chek Knuth's notes on this).

