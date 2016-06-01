import abc

class Player(Actor, metaclass=abc.ABCMeta):
    """A Player takes decisions, some other Actors can be random"""
    pass
