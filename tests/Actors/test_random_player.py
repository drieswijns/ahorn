import ahorn.TicTacToe as TTT
from ahorn.Actors import RandomPlayer
from tests.MockPlayer import MockPlayer

players = [RandomPlayer(), MockPlayer()]
def test_random_player():
    state = TTT.TTTState(players)
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
        # After 100 we expect that all legal actions should be chosen_action
        # at least once by the random player
        chosen_action = rp.get_action(state)
        chosen_actions.add(hash(chosen_action))
    
    assert(len(all_actions^chosen_actions) == 0)
