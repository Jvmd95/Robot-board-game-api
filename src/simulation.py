from src.robot import *
from src.dinosaur import *
from src.board import Board


class Simulation:
    """Represents the simulation.

    All the rules and commands that define the simulation are written here.

    Attributes
    ----------
    board : Board
        Board object that represents the board of the simulation

    Methods
    -------
    create_board() -> None:
        Initiates a Board object in self.board
    robot_instructions(robot_name: string, command: string) -> None:
        Passes commands to a robot.
        Commands can be "turn right", "turn left", "move forward", "move backward", "attack"
    create_robot(robot_name: string, robot_position: tuple, direction: string)
        Creates a robot of name robot_name in robot_position ie (1, 5) facing a direction.
        Directions can be "N", "S", "W", "E"
    create_dinosaur(dinosaur_position: tuple)
        Creates a dinosaur in dinosaur_position ie (1, 6).
    """

    def __init__(self):
        self.board = None

    def create_board(self):

        self.board = Board()

    def _move(self, robot, robot_position, target_position):
        robot.row, robot.column = target_position[0], target_position[1]
        self.board.board[target_position[0]][target_position[1]] = robot
        self.board.board[robot_position[0]][robot_position[1]] = None
        print(str(robot.name) + " moved.")

    def _move_forward(self, robot, robot_position):

        if robot.direction == "N":
            target_position = (robot_position[0] - 1, robot_position[1])

        elif robot.direction == "S":
            target_position = (robot_position[0] + 1, robot_position[1])

        elif robot.direction == "E":
            target_position = (robot_position[0], robot_position[1] + 1)

        else:
            target_position = (robot_position[0], robot_position[1] - 1)

        _is_valid_move(self.board, target_position)
        self._move(robot, robot_position, target_position)

    def _move_backward(self, robot, robot_position):

        if robot.direction == "N":
            target_position = (robot_position[0] + 1, robot_position[1])

        elif robot.direction == "S":
            target_position = (robot_position[0] - 1, robot_position[1])

        elif robot.direction == "E":
            target_position = (robot_position[0], robot_position[1] - 1)

        else:
            target_position = (robot_position[0], robot_position[1] + 1)

        _is_valid_move(self.board, target_position)
        self._move(robot, robot_position, target_position)

    def _attack(self, robot_position):

        target_position_n = (robot_position[0] - 1, robot_position[1])

        target_position_s = (robot_position[0] + 1, robot_position[1])

        target_position_e = (robot_position[0], robot_position[1] + 1)

        target_position_w = (robot_position[0], robot_position[1] - 1)

        targets = [target_position_n, target_position_s, target_position_e, target_position_w]

        for target in targets:
            target_piece = self.board.board[target[0]][target[1]]

            if target_piece:
                if target_piece.type == "D":
                    self.board.board[target[0]][target[1]] = None
                    print(f"Dinosaur at {target[0]}, {target[1]} destroyed! Well done.")

    def robot_instructions(self, robot_name: str, command: str):
        """
        Searches in all the robot instances for a robot with the same name.
        If found it gets its position on the board,
        then executes the command calling the corresponding private function.

        robot_name : str
            Name of the robot you want to give commands to
        command : str
            Commands can be "turn right", "turn left", "move forward", "move backward", "attack"
        """

        robot = _find_robot(robot_name)
        robot_position = (robot.row, robot.column)

        if command == "turn left":
            robot.turn_left()

        elif command == "turn right":
            robot.turn_right()

        elif command == "move forward":
            self._move_forward(robot, robot_position)

        elif command == "move backward":
            self._move_backward(robot, robot_position)

        elif command == "attack":
            self._attack(robot_position)

        else:
            raise Exception("Invalid command."
                            "List of valid commands ['turn left', 'turn right', 'move forward', 'move backward', "
                            "'attack']")

    # CREATE
    def create_robot(self, robot_name: str, robot_position: tuple, direction: str):
        """Creates a robot

        robot_name : str
            Name of the robot you want to create. Names need to be unique.
        robot_position : tuple
            Tuple representing the position on the board where you want the robot to be deployed.
            X and Y need to be in range [0-50] ie valid: (10,20), invalid: (60,20)
        direction : str
            Direction you want your dinosaur to be facing. Options are "N", "S", "W", "E"
        """
        _is_valid_name(robot_name)
        _is_valid_create_position(self.board, robot_position)
        robot = Robot(robot_name, robot_position[0], robot_position[1], direction)
        self.board.board[robot_position[0]][robot_position[1]] = robot

    def create_dinosaur(self, dinosaur_position: tuple):
        """Creates a dinosaur

        dinosaur_position : tuple
            Tuple representing the position on the board where you want the dinosaur to be deployed.
            X and Y need to be in range [0-50] ie valid: (10,20), invalid: (60,20)
        """
        _is_valid_create_position(self.board, dinosaur_position)
        dino = Dinosaur(dinosaur_position[0], dinosaur_position[1])
        self.board.board[dinosaur_position[0]][dinosaur_position[1]] = dino


'''''''''''''''''''''
Helper private functions
'''''''''''''''''''''


def _is_valid_position(position):
    if not (0 <= position[0] <= 50 and 0 <= position[1] <= 50):
        return False
    else:
        return True


def _is_valid_robot(robot):
    if robot is None:
        return False, None
    elif robot.type == "D":
        return False, "D"
    else:
        return True, None


def _is_valid_name(robot_name):
    for robot in Robot.instances:
        if robot.name == robot_name:
            raise Exception("Invalid robot name. There is already another robot with that name")


def _find_robot(robot_name):
    for robot in Robot.instances:
        if robot.name == robot_name:
            return robot

    raise Exception("Invalid robot name. There are no robots with that name on the board")


def _is_valid_target(board, target_position):
    if _is_valid_position(target_position) is False:
        return False, "invalid position"

    target_piece = board.board[target_position[0]][target_position[1]]

    if target_piece is not None:
        if target_piece.type == "D":
            return False, "D"
        if target_piece.type == "R":
            return False, "R"
    else:
        return True, None


def _is_valid_move(board, target_position):
    legal, details = _is_valid_target(board, target_position)
    if legal is False:
        if details == "invalid position":
            raise Exception("Robots are no cowards! You cant leave the battlefield.")
        elif details == "R":
            raise Exception("There is another robot in your path.")
        else:
            raise Exception("There is a dinosaur in your path. Kill it first if you want to advance.")


def _is_valid_create_position(board, create_position):
    legal, details = _is_valid_target(board, create_position)
    if legal is False:
        if details == "invalid position":
            raise Exception("Invalid creation position. X and Y must be inside the range [0-50]"
                            "ie (1,1) valid, (55,0) not valid")
        elif details == "R":
            raise Exception("There is a robot on that cell. Choose another cell.")
        else:
            raise Exception("There is a dinosaur on that cell. Choose another cell.")
