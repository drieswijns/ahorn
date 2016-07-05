from ahorn.TicTacToe.States import TicTacToeState
from ahorn.Actors import RandomPlayer, MCTSPlayer
from ahorn import Controller

players = [RandomPlayer(), MCTSPlayer()]
def test_mcts_player():
    average_utility = [0, 0]
    N = 10
    for _ in range(N):
        state = TicTacToeState(players)
        controller = Controller(state, verbose=True)
        end_state = controller.play()
        end_utility = [end_state.get_utility(p) for p in players]
        average_utility = [
            old + new
            for old, new
            in zip(average_utility, end_utility)
        ]
    average_utility = [j/N for j in average_utility]
    # MCTSPlayer should be better than RandomPlayer
    assert(average_utility[1] > average_utility[0])
