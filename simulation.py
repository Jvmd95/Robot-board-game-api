from robot import *
from dinosaur import *
from board import Board


class Simulation:

    def __init__(self):
        self.board = None

    def create_board(self):

        self.board = Board()

    # LEGALITY
    def _is_valid_position(self, position):
        if not (0 <= position[0] <= 50 and 0 <= position[1] <= 50):
            return False
        else:
            return True

    def _is_valid_robot(self):
        if self.robot is None:
            return False, None
        elif self.robot.name == "D":
            return False, "D"
        else:
            return True, None

    def _is_valid_target(self, target_position):

        if self._is_valid_position(target_position) is False:
            return False, "invalid position"

        target_piece = self.board.board[target_position[0]][target_position[1]]

        if target_piece is not None:
            if target_piece.name == "D":
                return False, "D"
            if target_piece.name == "R":
                return False, "R"
        else:
            return True, None

    def _is_valid_move(self, target_position):
        legal, details = self._is_valid_target(target_position)
        if legal is False:
            if details == "invalid position":
                raise Exception("Robots are no cowards! You cant leave the battlefield.")
            elif details == "R":
                raise Exception("There is another robot in your path.")
            else:
                raise Exception("There is a dinosaur in your path. Kill it first if you want to advance.")

    def _is_valid_create_position(self, create_position):
        legal, details = self._is_valid_target(create_position)
        if legal is False:
            if details == "invalid position":
                raise Exception("Invalid creation position. X and Y must be inside the range [0-50]"
                                "ie (1,1) valid, (55,0) not valid")
            elif details == "R":
                raise Exception("There is a robot on that cell. Choose another cell.")
            else:
                raise Exception("There is a dinosaur on that cell. Choose another cell.")

    # MOVEMENT
    def _move(self, robot_position, target_position):
        self.board.board[target_position[0]][target_position[1]] = self.robot
        self.board.board[robot_position[0]][robot_position[1]] = None
        print(str(self.robot) + " moved.")

    def _move_forward(self, robot_position):

        if self.robot.direction == "N":
            target_position = (robot_position[0] - 1, robot_position[1])

        elif self.robot.direction == "S":
            target_position = (robot_position[0] + 1, robot_position[1])

        elif self.robot.direction == "E":
            target_position = (robot_position[0], robot_position[1] + 1)

        else:
            target_position = (robot_position[0], robot_position[1] - 1)

        self._is_valid_move(target_position)
        self._move(robot_position, target_position)

    def _move_backward(self, robot_position):

        if self.robot.direction == "N":
            target_position = (robot_position[0] + 1, robot_position[1])

        elif self.robot.direction == "S":
            target_position = (robot_position[0] - 1, robot_position[1])

        elif self.robot.direction == "E":
            target_position = (robot_position[0], robot_position[1] - 1)

        else:
            target_position = (robot_position[0], robot_position[1] + 1)

        self._is_valid_move(target_position)
        self._move(robot_position, target_position)

    def attack(self, robot_position):

        target_position_n = (robot_position[0] - 1, robot_position[1])

        target_position_s = (robot_position[0] + 1, robot_position[1])

        target_position_e = (robot_position[0], robot_position[1] + 1)

        target_position_w = (robot_position[0], robot_position[1] - 1)

        targets = [target_position_n, target_position_s, target_position_e, target_position_w]

        for target in targets:
            target_piece = self.board.board[target[0]][target[1]]

            if target_piece:
                if target_piece.name == "D":
                    self.board.board[target[0]][target[1]] = None
                    print(f"Dinosaur at {target[0]}, {target[1]} destroyed! Well done.")

    # COMMAND CENTRAL
    def robot_instructions(self, robot_position, command):

        if self._is_valid_position(robot_position) is False:
            raise Exception("Invalid position on board")

        # Possible mistake to declare self.robot here, instead carry it in functions
        self.robot = self.board.board[robot_position[0]][robot_position[1]]

        legal, details = self._is_valid_robot()
        if legal is False:
            if details is None:
                raise Exception("There is nothing there!")
            else:
                raise Exception("That is a dinosaur. Dinosaurs obey no instructions!")

        if command == "turn left":
            self.robot.turn_left()

        elif command == "turn right":
            self.robot.turn_right()

        elif command == "move forward":
            self._move_forward(robot_position)

        elif command == "move backward":
            self._move_backward(robot_position)

        elif command == "attack":
            self.attack(robot_position)

        else:
            raise Exception("Invalid command."
                        "List of valid commands ['turn left', 'turn right', 'move forward', 'move backward', 'attack']")

    # CREATE
    def create_robot(self, robot_position, direction):
        self._is_valid_create_position(robot_position)
        robot = Robot(robot_position[0], robot_position[1], direction)
        self.board.board[robot_position[0]][robot_position[1]] = robot

    def create_dinosaur(self, dinosaur_position):
        self._is_valid_create_position(dinosaur_position)
        dino = Dinosaur(dinosaur_position[0], dinosaur_position[1])
        self.board.board[dinosaur_position[0]][dinosaur_position[1]] = dino







