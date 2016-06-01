import abc

class Action(metaclass=abc.ABCMeta):
    """An action modifies one game state into the other."""
    @abc.abstractmethod
    def __init__(self):
        """Initialise an action.

        Parameters
        ----------

        Returns
        -------
        """
        pass

    @abc.abstractmethod
    def execute(self, state):
        """Perform the action on a given state

        Parameters
        ----------
        State:
            The state that must be modified

        Returns
        -------
        State:
            The modified state
        """
        pass
