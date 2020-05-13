"""
    sphinx_ext.pylit
    ~~~~~~~~~~~~~~~~

    Sphinx Directives to support Literate Programming.

    Copyright 2018-2020 by Roie R. Black
"""
from typing import Any, Dict, List, Tuple

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.nodes import Element, Node
from docutils.statemachine import StringList

from sphinx.domains.std import StandardDomain
from sphinx.util.docutils import SphinxDirective

def container_wrapper(directive: SphinxDirective, literal_node: Node, caption: str) -> nodes.container:  # NOQA
    container_node = nodes.container('', literal_block=True,
                                     classes=['literal-block-wrapper'])
    parsed = nodes.Element()
    directive.state.nested_parse(StringList([caption], source=''),
                                 directive.content_offset, parsed)
    if isinstance(parsed[0], nodes.system_message):
        msg = __('Invalid caption: %s' % parsed[0].astext())
        raise ValueError(msg)
    elif isinstance(parsed[0], nodes.Element):
        caption_node = nodes.caption(parsed[0].rawsource, '',
                                     *parsed[0].children)
        caption_node.source = literal_node.source
        caption_node.line = literal_node.line
        container_node += caption_node
        container_node += literal_node
        return container_node
    else:
        raise RuntimeError  # never reached

class pylit_node(nodes.General, nodes.Element):
    pass

class pylitlist(nodes.General, nodes.Element):
    pass

class PylitBlock(SphinxDirective):

    node_class = pylit_node
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_whitespace = False
    option_spec = {
            'linenos': directives.flag,
            'caption': directives.unchanged_required,
    }

    def run(self) -> List[Node]:
        env = self.state.document.settings.env

        language = self.arguments[0].lower()
        block_type = self.name.split(':')[1]

        caption = self.options.get('caption')
        if not caption:
            caption = "unnamed block"
        if block_type == 'file':
            caption = '<<%s>>==' % caption
        elif block_type == 'code':
            caption = '<<%s>>==' % caption
        elif block_type == 'add':
            caption = '<<%s>>+=' % caption
        elif block_type == 'file':
            caption = '<<file: %s>>==' % caption
        elif block_type == 'shell':
            caption = '<<shell: %s>>==' % caption


        code = '\n'.join(self.content)
        literal = nodes.literal_block(code, code)
        if self.arguments:
            literal['language'] = self.arguments[0]
        else:
            literal['language'] = 'python'
        try:
            literal = container_wrapper(self, literal, caption)
        except ValueError as exc:
            return [document.reporter.warning(exc, line = self.lineno)]
        self.add_name(literal)
        return [literal]

class PylitDomain(StandardDomain):
    name = "pylit"
    label = "Pylit Block"

    directives = {
        "file": PylitBlock,
        "code": PylitBlock,
        "add": PylitBlock,
        "shell": PylitBlock,
    }

class PylitList(SphinxDirective):

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self) -> List[Node]:
        return [pylitlist('')]
def setup(app: "Pylit") -> Dict[str, Any]:
    app.add_domain(PylitDomain)

    return {
        'version': '0.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
