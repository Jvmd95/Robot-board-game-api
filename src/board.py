class Board:
    """A class to represent a board.

    The board is simulated by an array of arrays.
    The board is initialized with null values in every cell,
    which can then be populated by either the robot or dinosaur class objects.

    Attributes
    ----------
    board : list[list[Piece]]
        Array of arrays that simulate a board
    """

    def __init__(self):
        self.board = []
        self._create_board()

    def _create_board(self):

        for i in range(50):
            self.board.append([None] * 50)
