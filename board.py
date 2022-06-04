class Board:

    def __init__(self):
        self.board = []
        self._create_board()

    def _create_board(self):

        for i in range(50):
            self.board.append([None] * 50)

    def print_board(self):
        """
        Prints the current state of the board.
        """
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                if j is None:
                    tmp_str += "   |"
            print(tmp_str)