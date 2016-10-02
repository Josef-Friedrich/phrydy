import sphinx_rtd_theme
import phrydy
VERSION = phrydy.__version__
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]
templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

project = u'phrydy'
copyright = u'2016, Josef Friedrich'
author = u'Josef Friedrich'
version = VERSION
release = VERSION
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_static_path = []
htmlhelp_basename = 'phrydydoc'

latex_elements = {
     'papersize': 'a4paper',
     'pointsize': '11pt',
}

latex_documents = [
    (master_doc, 'phrydy.tex', u'phrydy Documentation',
     u'Josef Friedrich', 'manual'),
]

man_pages = [
    (master_doc, 'phrydy', u'phrydy Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'phrydy', u'phrydy Documentation',
     author, 'phrydy', 'One line description of project.',
     'Miscellaneous'),
]
