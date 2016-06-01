from distutils.core import setup

setup(
  name = 'ahorn',
  packages = ['ahorn'], # this must be the same as the name above
  version = '0.1',
  description = 'A game playing and game AI library',
  author = 'Dries Wijns',
  author_email = 'dries.wijns@gmail.com',
  url = 'TODO', # use the URL to the github repo
  download_url = 'TODO', # I'll explain this in a second
  keywords = ['game', 'playing', 'AI'], # arbitrary keywords
  classifiers = [],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  package_data={"ahorn": ["ahorn/*"]},

)
