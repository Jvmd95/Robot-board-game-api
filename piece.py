class Piece:
    ICONS = {
        "BK": "&#9818;",
        "BQ": "&#9819;",
        "BR": "&#9820;",
        "BB": "&#9821;",
        "BN": "&#9822;",
        "BP": "&#9823;",
        "WK": "&#9812;",
        "WQ": "&#9813;",
        "WR": "&#9814;",
        "WB": "&#9815;",
        "WN": "&#9816;",
        "WP": "&#9817;"
    }

    def __init__(self, row, column, label="", icon=""):
        self.row = row  # row
        self.column = column  # column
        self.taken = False
        self.label = label
        self.icon = icon

    def is_legal_move(self, target, chessboard):
        raise NotImplementedError()

    def is_taken(self):
        return self.taken

    def set_as_taken(self):
        self.taken = True
        self.update_position(-1, -1)

    def update_position(self, row, column):
        self.row = row
        self.column = column

    @classmethod
    def icon(cls, label):
        if label in cls.ICONS:
            return cls.ICONS[label]
        else:
            return ""