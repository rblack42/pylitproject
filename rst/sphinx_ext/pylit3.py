"""
    sphinx.ext.pylit
    ~~~~~~~~~~~~~~~~

    Allow tagged versions of a git repository to be fetched into a specified
    directory, then allow fetched files from those versions to be included
    in a document.  Also allow commands to be run against the fetched version of a
    project. Initial support for literate programming


    :copyright: Copyright 2020 by Roie Black
    :license: BSD, see LICENSE for details.
"""


from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util.docutils import SphinxDirective
from sphinx.locale import _, __

class pylit(nodes.General, nodes.Element):
    pass

class pylitlist(nodes.General, nodes.Element):
    pass

def visit_pylit_node(self, node):
    self.visit_adminition(node)


def depart_pylit_node(node):
    self.depart_adminition(node)

class PylitListDirective(SphinxDirective):

    def run(self):
        return [pylitlist('')]

class PyLit(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        env = self.state.document.settings.env

        targetid = 'pylit-%d' % env.new_serialno('pylit')
        targetnode = nodes.target('', '', ids=[targetid])

        pylit_node = pylit('\n'.join(self.content))
        pylit_node += nodes.title(_('Pylit'), _('Pylit'))

        if not hasattr(env, 'pylit_blocks'):
            env.pylit_blocks = []
            env.pylit_block_num = 1
        env.pylit_blocks.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'block': pylit_node.deepcopy(),
            'blknum': env.pylit_block_num,
        })
        env.pylit_block_num += 1

        text = "PyLiT is running\n"
        sandbox = self.arguments[0]
        sandbox_path = env.relfn2path(sandbox)[1]
        text += "Sandox path:" + sandbox_path + "\n"
        paragraph_node = nodes.paragraph(text=text)
        return [paragraph_node]

def setup(app):
    app.add_node(pylit)
    app.add_directive("pylit", PyLit)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
