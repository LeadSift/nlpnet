import sys
from distutils.core import setup
from distutils.extension import Extension

def readme():
    with open('README.rst') as f:
        text = f.read()
    return text

setup(
      name = 'nlpnet',
      description = 'Neural networks for NLP tasks',
      packages = ['nlpnet', 'nlpnet.pos', 'nlpnet.srl'],
      ext_modules = [Extension("nlpnet.network", 
                               ["nlpnet/network.c"],
                               include_dirs=['.', np.get_include()]
                               )
                     ],
      scripts = ['bin/nlpnet-tag.py',
                 'bin/nlpnet-train.py',
                 'bin/nlpnet-test.py',
                 'bin/nlpnet-load-embeddings.py'],
      license = 'MIT',
      version = '1.1.4',
      author = 'Erick Fonseca',
      author_email = 'erickrfonseca@gmail.com',
      url = 'http://nilc.icmc.usp.br/nlpnet',
      install_requires = [
        'nltk',
        'numpy',
      ],
      long_description = readme()
      )
