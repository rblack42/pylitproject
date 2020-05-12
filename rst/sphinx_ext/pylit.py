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
from sphinx.util.docutils import SphinxDirective


class PylitBlock(SphinxDirective):

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_whitespace = False
    option_spec = {
            'linenos': directives.flag,
            'caption': directives.unchanged,
    }

    def run(self) -> List[Node]:
        code = '\n'.join(self.content)
        literal = nodes.literal_block(code, code)
        return [literal]

def setup(app: "Pylit") -> Dict[str, Any]:
    directives.register_directive('pylit', PylitBlock)

    return {
        'version': '0.0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
