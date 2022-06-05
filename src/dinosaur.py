class Dinosaur:
    """Represents a dinosaur.

    Attributes
    ----------
    row : int
        Integer representing the row the dinosaur is located at.
    column : int
        Integer representing the column the dinosaur is located at.
    type : str
        An identification string indicating that the object is indeed a dinosaur.
    html_icon : str
        An unicode string. Is used to display a dinosaur image in the board.
    """

    def __init__(self, row: int, column: int):
        """Inits Dinosaur with row, column, name and html_icon"""
        self.row = row  # row
        self.column = column  # column
        self.type = "D"
        self.html_icon = "&#x1F996;"
