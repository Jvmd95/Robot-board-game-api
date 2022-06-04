class Robot:

    def __init__(self, row, column, direction):
        self.row = row  # row
        self.column = column  # column
        self.taken = False
        self.name = "R"
        self.direction = direction

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        else:
            self.direction = "N"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"

    def attack(self):
        pass





