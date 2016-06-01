from ..GameBase.State import State as BaseState
from .TTTActions import TTTAction

class TTTState(BaseState):
    """Describes a Tic-Tac-Toe state"""
    def __init__(self, players):
        """Initialise a Tic-Tac-Toe state

        Parameters
        ----------
        players: List
            A list of Player objects

        Returns
        -------
        """
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.players = players
        self.pi = 0  # index of the current players

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

        for i, row in enumerate(other.board):
            for j, item in enumerate(row):
                this.board[i][j] = item
        this.pi = other.pi

    def _find_success(self):
        """Find OOO or XXX rows.

        Parameters
        ----------

        Returns
        -------
        row: List
            Either OOO or XXX, depending in which one has been found.
            Or None if none found"""
        def _row_identical(a, b):
            return all([
                aa == bb
                for aa, bb in zip(a, b)
            ])

        ooo = ["O", "O", "O"]
        xxx = ["X", "X", "X"]


        for row in self.board:  # check all the rows
            if _row_identical(row, ooo):
                return ooo
            if _row_identical(row, xxx):
                return xxx

        transpose = zip(*self.board)
        for collumn in transpose:  # check all the collumns
            if _row_identical(collumn, ooo):
                return ooo
            if _row_identical(collumn, xxx):
                return xxx

        diagonals = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        ]
        for diagonal in diagonals:
            if _row_identical(diagonal, ooo):
                return ooo
            if _row_identical(diagonal, xxx):
                return xxx

        return None

    def is_final(self):
        """Return true if there is an OXO on the board, or the board is full.

        Parameters
        ----------

        Returns
        -------
        bool
            True if the state is an OXO on the board, false otherwise"""

        if self._find_success:  # OOO or XXX found, game is over
            return True

        free_spots = sum([
            1 if item == "-" else 0
            for row in self.board
            for item in row
        ])
        if free_spots == 0:  # no more free spots, game is over
            return True

        return False

    def get_random(self, player):
        """Tic-Tac-Toe is of complete information. Return a copy of this state.

        Parameters
        -----------
        player: Player
            Not used

        Returns
        -------
        State
            A copy of this state"""
        new = TTTState(this.players)
        new.copy(this)
        return new

    def get_actor(self):
        """Return the actor that must perform an action in this state.

        Cycles between the first player and the second player

        Parameters
        ----------

        Returns
        -------
        Actor
            The player that must perform an action in this state."""
        return this.players[this.pi]

    def get_legal_actions(self, player):
        """Return the legal actions a player can take in this state.

        Parameters
        ----------
        player: Player
            the player who wants to know which actions he can take

        Returns
        -------
        actions: List
            a list of Actions"""
        symbol = ["O", "X"][this.players.index(player)]

        legal_actions = []
        for j, row in enumerate(this.board):
            for k, item in enumerate(row):
                if item == "-":
                    legal_actions.append(
                        TTTAction(
                            symbol=symbol,
                            where=(j, k)
                        )
                    )
        return legal_actions

    def get_utility(self, player):
        """Return +1 if player won, -1 if player lost, 0 if draw.

        If the state is final, returns the utility, else returns None

        Parameters
        ----------
        player: Player
            The player for which to find the utility

        Returns
        -------
        utility: int
            The utility received by the player, or None"""
        if not this.is_final():
            return None

        success = this._find_success()
        if success:
            aim = ["O", "X"][this.players.index(player)]
            if success[0] == aim:
                return 1  # player achieved his goal and won
            else:
                return -1  # other player achieved his goal and won
        return 0

    def __str__(self):
        """Returns a string containing the board, and the current player

        Parameters
        ----------

        Returns
        -------
        str
            String representation of this state."""
        s = "Tic-Tac-Toe: \n"
        for row in this.board:
            s += "\t"+" ".join(row)+"\n"
        s += "Player {}'s turn".format(this.pi)

    def __hash__(self):
        """Hash of the current state.

        Parameters
        ----------

        Returns
        -------
        int
            The hash of the state"""
        return hash(str(self))
