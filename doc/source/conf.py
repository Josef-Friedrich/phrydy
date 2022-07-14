import sphinx_rtd_theme

import phrydy

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

project = 'phrydy'
copyright = '2016, Josef Friedrich'
author = 'Josef Friedrich'
version = phrydy.__version__
release = phrydy.__version__
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_static_path = []
htmlhelp_basename = 'phrydydoc'
autodoc_default_flags = ['members', 'undoc-members', 'private-members', 'show-inheritance']
