#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

conf
====

Generation of documentation.

"""

from os.path import abspath
from sys import path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, List, Tuple, Union

path.insert(0, abspath("./../src"))

# pylint: disable=wrong-import-position, unused-import,
import swinging_door  # noqa: E402, F401

# pylint: disable=invalid-name, redefined-builtin

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]  # type: List[str]

source_suffix = ".rst"  # type: str
master_doc = "index"  # type: str

autodoc_default_options = {
    "private-members": True,
    "special-members": "__init__, __repr__, __str__, __call__",
    "show-inheritance": True,
    "members": True,
    "exclude-members": "__weakref__",
}  # type: Dict[str, Union[bool, str]]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}  # type: Dict[str, Tuple[str, None]]
todo_include_todos = True  # type: bool

project = "swinging_door"  # type: str
author = "Aleksandr F. Mikhaylov (ChelAxe) <chelaxe@gmail.com>"  # type: str
copyright = "D.F.H. ChelAxe 2005"  # type: str
version = swinging_door.__version__  # type: str
release = swinging_door.__version__  # type: str
language = "en"  # type: str
show_authors = True  # type: bool

html_theme = "alabaster"  # type: str
html_show_sourcelink = False  # type: bool
html_show_copyright = False  # type: bool
html_experimental_html5_writer = True  # type: bool
html_theme_options = {
    "logo": "images/logo.png",
    "description": "Swinging Door",
    "fixed_sidebar": True,
    "sidebar_collapse": True,
    "show_powered_by": False,
    "show_relbars": True,
}  # type: Dict[str, Union[str, bool]]

html_static_path = ["_static"]  # type: List[str]
html_css_files = ["css/style.min.css"]  # type: List[str]
html_js_files = ["js/script.min.js"]  # type: List[str]
html_favicon = "_static/favicon.ico"  # type: str
mathjax_path = "js/MathJax/MathJax.js"  # type: str

latex_paper_size = "a4"  # type: str
latex_logo = "_static/images/logo.png"  # type: str
latex_font_size = "14pt"  # type: str
latex_documents = [
    (
        "index",
        "swinging_door.tex",
        "swinging_door",
        "Aleksandr F. Mikhaylov (ChelAxe) <chelaxe@gmail.com>",
        "howto",
    )
]  # type: List[Tuple[str, str, str, str, str]]
