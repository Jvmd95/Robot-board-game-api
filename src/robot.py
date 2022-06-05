class Robot:
    """Represents a robot.

    Attributes
    ----------
    row : int
        Integer representing the row the robot is located at.
    column : int
        Integer representing the column the robot is located at.
    direction : str
        String that indicates the direction our robot is looking at. N, S, W, E
    name : str
        An identification string indicating that the object is indeed a robot.
    html_icon : str
        An unicode string. Is used to display a robot image in the board.

    Methods
    -------
    turn_left():
        Turns our robot to its left
    turn_right():
        Turns our robot to its right
    """

    instances = []

    def __init__(self, name, row, column, direction):
        """Inits Robot with row, column, direction, name and html_icon"""
        self.__class__.instances.append(self)
        self.name = name
        self.row = row
        self.column = column
        self.direction = direction
        self.type = "R"
        self.html_icon = "&#129302;"

    def turn_left(self):
        """Turns our robot to the left"""
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        else:
            self.direction = "N"

    def turn_right(self):
        """Turns our robot to the right"""
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"
