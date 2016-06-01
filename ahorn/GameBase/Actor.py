import abc

class Actor(metaclass=abc.ABCMeta):
    """An actor performs actions and drives a game from state to state."""
    @abc.abstractmethod
    def __init__(self):
        """Initialise an actor.

        Parameters
        ----------

        Returns
        -------
        """
        pass

    @abc.abstractmethod
    def get_action(self, state):
        """Return the action the actor wants to take in a given state.

        Parameters
        ----------
        State:
            The state in which the actor must perform an action

        Returns
        -------
        Action:
            The action the actor wants to take in this state."""
        pass
