import os
import sys

sys.path.insert(0, os.path.abspath('.'))

master_doc = 'bug.base'

language = 'ru'
# language = 'en'  # works fine without blockquote wrapper

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

html_title = 'Sphinx Bases Bug'
