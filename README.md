Ahorn
===================

A game description framework and game playing AI library.

Quickstart
==========
  >>> import ahorn, ahorn.Actors, ahorn.TicTacToe
  >>> player_a, player_b = ahorn.Actors.MCTSPlayer(), ahorn.Actors.MCTSPlayer()
  >>> starting_state = ahorn.TicTacToe.TicTacToeState([player_a, player_b])
  >>> controller = ahorn.Controller(starting_state, verbose=True)
  >>> controller.play()

Adding a new game
=================

A game is described by states and actions.
To describe a new game, subclass ahorn.GameBase.State and ahorn.GameBase.Action.
Take a look at the example game ahorn.TicTacToe.

Adding new AI
=============

ahorn comes with a generic AI based on the Monte Carlo Tree Search algorithm:
 ahorn.Actors.MCTSPlayer.
To exeriment with new AI, subclass ahorn.GameBase.Player, Take a look at the
example AI ahorn.Actors.RandomPlayer.
