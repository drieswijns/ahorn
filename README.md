Ahorn
===================

A game description framework and game playing AI library,
written entirely in Python.
Designed for ease-of-use and extensibility. If you're looking for performance,
ahorn might not be for you.

Quickstart
==========
    import ahorn, ahorn.Actors, ahorn.TicTacToe
    player_a, player_b = ahorn.Actors.MCTSPlayer(), ahorn.Actors.MCTSPlayer()
    starting_state = ahorn.TicTacToe.TicTacToeState([player_a, player_b])
    controller = ahorn.Controller(starting_state, verbose=True)
    controller.play()

Documentation
=============
Documentation can be found on [read the docs](http://ahorn.readthedocs.io/en/latest/)

Installation
============
    pip install ahorn

or

    git clone https://github.com/drieswijns/ahorn
    pip3 install -r requirements.txt
    python3 setup.py install
    python3 run.py  # start playing a game

Running the tests
=================
    python3 -m pytest tests

Adding a new game
=================

A game is described by states and actions.
To describe a new game, subclass the following base classes

    ahorn.GameBase.State  
    ahorn.GameBase.Action

Take a look at  

    ahorn.TicTacToe

for an example.

Or follow the in-depth [minesweeper tutorial](https://github.com/drieswijns/ahornsweeper).

Adding new AI
=============

Ahorn comes with a generic AI based on the Monte Carlo Tree Search algorithm:  

    ahorn.Actors.MCTSPlayer

To create a new AI, subclass  

    ahorn.GameBase.Player

Take a look at  

    ahorn.Actors.RandomPlayer

for an example.

Or follow the in-depth [minesweeper tutorial](https://github.com/drieswijns/ahornsweeper).
