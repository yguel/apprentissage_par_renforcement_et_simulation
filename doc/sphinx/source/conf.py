# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Apprentissage par Renforcement et Simulation'
copyright = '2024, Manuel YGUEL'
author = 'Manuel YGUEL'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.bibtex",
    "sphinx_exercise",
    "sphinx_togglebutton",
    "rst2pdf.pdfbuilder",
]

myst_enable_extensions = ["colon_fence"]

numfig = True # Enable figure, table, code blocks numbering

# Optional: Customize the labels for different object types
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Tableau %s',
    'code-block': 'Listing %s',
    'download': 'Download %s',
    'section': 'Section %s',
}

bibtex_bibfiles = ['']

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = [".rst", ".md"]

rst_prolog = """
.. role:: underline
    :class: underline

.. |br| raw:: html

      <br>
"""

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_sidebars = {
    '**': [
        'globaltoc.html',   # Use the global TOC instead of the local one
        'relations.html',   # Adds links to the previous and next chapters
        'searchbox.html',   # Adds a search box
    ]
}

# -- Options for copybutton extension ----------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# -- Style options
from docutils import nodes
from docutils.parsers.rst import roles

def bold_underline_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.strong(text, text)
    node['classes'].append('underline')
    return [node], []

roles.register_local_role('bold_underlined', bold_underline_role)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_css_files = [
    "css/custom.css",
]