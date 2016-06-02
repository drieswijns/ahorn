from ahorn.TicTacToe.States import TicTacToeState
from ahorn.Actors import RandomPlayer
from tests.MockPlayer import MockPlayer

players = [RandomPlayer(), MockPlayer()]
def test_random_player():
    state = TicTacToeState(players)
    state.board = [
        ["X", "-", "X"],
        ["O", "-", "O"],
        ["X", "-", "X"]
    ]
    rp = players[0]
    all_actions = set([
        hash(a)
        for a
        in state.get_legal_actions(rp)
    ])

    chosen_actions = set()
    for _ in range(100):
        # After 100 samples we expect that all legal actions should be
        # chosen at least once by the random player
        chosen_action = rp.get_action(state)
        chosen_actions.add(hash(chosen_action))

    assert(len(all_actions^chosen_actions) == 0)
