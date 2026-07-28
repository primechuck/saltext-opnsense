import os
import sys
import datetime

sys.path.insert(0, os.path.abspath("../src"))

project = "saltext-opnsense"
copyright = f"{datetime.datetime.now().year}, David Bierce"
author = "David Bierce"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
