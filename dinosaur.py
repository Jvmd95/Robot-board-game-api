from piece import *


class Dinosaur(Piece):

    def __init__(self, row, column, label="", icon=""):
        super().__init__(row, column, label, icon)
        self.name = "D"