from ahorn.GameBase.Player import Player

class MockPlayer(Player):
    """An actor that does nothing."""
    def __init__(self):
        pass

    def get_action(self, state):
        pass
