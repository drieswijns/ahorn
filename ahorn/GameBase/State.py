import abc

class State(metaclass=abc.ABCMeta):
    """Describes the attributes of a game at a particular time"""
    @abc.abstractmethod
    def __init__(self):
        """Initialise a state

        Parameters
        ----------

        Returns
        -------"""
        pass

    @abc.abstractmethod
    def copy(self, other):
        """Copy the content of another state into this state

        Deep copy, i.e. modifying the copied state can not influence the
        content of the original state.

        Parameters
        ----------
        other : State
            The state from which to copy the content

        Returns
        -------"""
        pass

    @abc.abstractmethod
    def is_final(self):
        """Return true if the state is final, i.e. the game is over

        Parameters
        ----------

        Returns
        -------
        bool
            True if the state is final, false otherwise"""
        pass

    @abc.abstractmethod
    def get_random(self, player):
        """Get a random sample from the information set of the current state.

        This method can be used to hide certain attributes of the state, such
        as opponent's cards. In case of games with perfect information this
        information contains only the state itself, and a copy of the state
        itself is returned.

        Parameters
        -----------
        player: Player
            The information set is created from the point of view of this actor

        Returns
        -------
        State
            A random sample from the information set"""
        pass

    @abc.abstractmethod
    def get_actor(self):
        """Return the actor that must perform an action in this state.

        Parameters
        ----------

        Returns
        -------
        Actor
            The actor that must perform an action in this state."""
        pass

    @abc.abstractmethod
    def get_utility(self, player):
        """Return the utility a given player receives.

        If the state is final, returns a utility, else returns None

        Parameters
        ----------
        player: Player
            The player for which to find the utility

        Returns
        -------
        utility: int
            The utility received by the player, or None"""
        pass

    @abc.abstractmethod
    def __str__(self):
        """A string representation of this state.

        Parameters
        ----------

        Returns
        -------
        str
            String representation of this state."""
        pass

    @abc.abstractmethod
    def __hash__(self):
        """Get a hash of the current state.

        Parameters
        ----------

        Returns
        -------
        int
            The hash of the state"""
        pass
