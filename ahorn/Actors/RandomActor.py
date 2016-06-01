import random
from ..GameBase import Actor


class RandomActor(Actor):
    """An actor who always choses random actions."""
    def __init__(self):
        """Initialise the RandomActor.

        Parameters
        ----------

        Returns
        -------
        """
        pass

    def get_action(self, state):
        """Return a random action from the legal actions

        Parameters
        ----------
        State:
            The state in which the actor must perform an action

        Returns
        -------
        Action:
            A random action from the legal actions"""
        return random.choice(
            state.get_legal_actions(self)
        )
