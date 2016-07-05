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
