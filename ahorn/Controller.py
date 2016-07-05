class Controller(object):
    """A controller is used to play a game."""
    def __init__(self, initial_state, verbose=False):
        """Create a controller by providing players and a state

        Parameters
        ----------
        players: List
            List of Player objects
        inititial_state: State
            State object from which to start the game

        Returns
        -------
        """
        self.state = initial_state
        self.verbose = verbose

    def play(self):
        """Plays the game untill a final state is reached

        Parameters
        ----------

        Returns
        -------
        final_state: State
            The final state"""

        state = self.state
        while not state.is_final():
            actor = state.get_actor()
            if self.verbose: print(state.str(actor))
            action = actor.get_action(state.get_random(actor))
            state = action.execute(state)
            if self.verbose: print(str(action))
        self.state = state
        if self.verbose:
            print(state.str(actor))
            print("Points: {}".format(" ,".join([
                str(state.get_utility(player))
                for player in state.players
            ])))

        return self.state
