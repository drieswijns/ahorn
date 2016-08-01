from distutils.core import setup

setup(
  name = 'ahorn',
  packages = ['ahorn', 'ahorn.Actors', 'ahorn.GameBase', 'ahorn.TicTacToe'],
  version = '0.1',
  description = 'A game playing and game AI library',
  author = 'Dries Wijns',
  author_email = 'dries.wijns@gmail.com',
  url = 'TODO', # use the URL to the github repo
  download_url = 'TODO', # I'll explain this in a second
  keywords = ['game', 'playing', 'AI', 'MCTS'],
  classifiers = [],
  package_data={"ahorn": ["ahorn/*"]},
)
