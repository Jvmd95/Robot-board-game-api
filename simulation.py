from piece import *
from robot import *
from dinosaur import *
from board import Board


class Simulation:

    def __init__(self):

        self.board = Board()

    # COMMANDS
    def _is_valid_robot(self):
        if self.robot is None:
            raise Exception("There is no nothing there! Create a robot or a dino first")
        elif self.robot.name == "D":
            raise Exception("That is a dinosaur! You can only move robots")
        else:
            return

    def _is_valid_target(self, target_position):

        if not 0 <= target_position[0] <= 50 and 0 <= target_position[1] <= 50:
            raise Exception("Invalid move. Robot can not leave simulation space")

        target_piece = self.board.board[target_position[0]][target_position[1]]

        if target_piece is not None:
            if target_piece.name == "D":
                raise Exception("There is a dinosaur at the target position! Kill it first if you want to move there")
            if target_piece.name == "R":
                raise Exception("There is another robot at the target position!")
        else:
            return

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

        self._is_valid_target(target_position)
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

        self._is_valid_target(target_position)
        self._move(robot_position, target_position)

    def robot_instructions(self, robot_position, command):

        if not 0 <= robot_position[0] <= 50 and 0 <= robot_position[1] <= 50:
            raise Exception("Invalid position on board")

        # Possible mistake to declare self.robot here, instead carry it in functions
        self.robot = self.board.board[robot_position[0]][robot_position[1]]

        self._is_valid_robot()

        if command == "turn left":
            self.robot.turn_left()

        elif command == "turn right":
            self.robot.turn_right()

        elif command == "move forward":
            self._move_forward(robot_position)

        elif command == "move backward":
            self._move_backward(robot_position)

        elif command == "attack":
            pass

        else:
            "Invalid command"

    # CREATE
    def create_robot(self, robot_position, direction):
        robot = Robot(robot_position[0], robot_position[1], direction)
        target_piece = self.board.board[robot_position[0]][robot_position[1]]




