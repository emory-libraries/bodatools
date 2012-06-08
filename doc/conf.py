# bodatools documentation build configuration file

import bodatools

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

#templates_path = ['templates']
exclude_trees = ['build']
source_suffix = '.rst'
master_doc = 'index'

project = 'bodatools'
copyright = '2012, Emory University Libraries'
version = '%d.%d' % bodatools.__version_info__[:2]
release = bodatools.__version__
modindex_common_prefix = ['bodatools.']

pygments_style = 'sphinx'

html_style = 'default.css'
#html_static_path = ['static']
htmlhelp_basename = 'eulcoredoc'

latex_documents = [
  ('index', 'bodatools.tex', 'bodatools Documentation',
   'Emory University Libraries', 'manual'),
]


# configuration for intersphinx: refer to the Python standard library
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
}
