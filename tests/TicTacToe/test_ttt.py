from ahorn.TicTacToe import TTTAction, TTTState
from ahorn import Controller
from ahorn.Actors import RandomPlayer

from tests.MockPlayer import MockPlayer as MockPlayer

players = [MockPlayer(), MockPlayer()]

def test_get_legal_actions_one_action():
    state = TTTState(players)
    state.board = [
        ["X", "O", "X"],
        ["O", "-", "O"],
        ["X", "O", "X"]
    ]
    la = state.get_legal_actions(players[0])
    assert(len(la) == 1)
    la = la[0]
    assert(la.symbol == "O")
    assert(la.where[0] == 1)
    assert(la.where[1] == 1)

    la = state.get_legal_actions(players[1])
    assert(len(la) == 1)
    la = la[0]
    assert(la.symbol == "X")
    assert(la.where[0] == 1)
    assert(la.where[1] == 1)

def test_get_legal_actions_two_actions():
    state = TTTState(players)
    state.board = [
        ["X", "O", "X"],
        ["O", "-", "-"],
        ["X", "O", "X"]
    ]
    la = state.get_legal_actions(players[0])
    assert(len(la) == 2)

def test_tttaction():
    state = TTTState(players)
    state.board = [
        ["X", "O", "X"],
        ["O", "-", "-"],
        ["X", "O", "X"]
    ]
    action = TTTAction(
        symbol="O",
        where=(1, 1)
    )
    state = action.execute(state)
    expected_board = [
        ["X", "O", "X"],
        ["O", "O", "-"],
        ["X", "O", "X"]
    ]
    for row, exp_row in zip(state.board, expected_board):
        for item, exp_item in zip(row, exp_row):
            assert(item == exp_item)

def test_is_final_full_board():
    state = TTTState(players)
    state.board = [
        ["X", "O", "X"],
        ["O", "0", "X"],
        ["X", "X", "O"]
    ]
    assert(state.is_final())

def test_is_final_success():
    state = TTTState(players)
    state.board = [
        ["X", "-", "X"],
        ["O", "-", "X"],
        ["X", "-", "X"]
    ]
    assert(state.is_final())

def test_is_final_negative():
    state = TTTState(players)
    state.board = [
        ["X", "-", "X"],
        ["O", "-", "-"],
        ["X", "-", "X"]
    ]
    assert(not state.is_final())

def test_full_games():
    # Play 10 full games without crashing
    players = [RandomPlayer(), RandomPlayer()]
    for _ in range(10):
        s = TTTState(players)
        c = Controller(s)
        s = c.play()
        assert(s.is_final())  # game should have ended
        assert(  # game is zero-sum
            s.get_utility(players[0]) + s.get_utility(players[1]) == 0
        )
