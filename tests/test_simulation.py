import pytest
from src.simulation import Simulation


def test_create_board():
    sim = Simulation()
    sim.create_board()
    assert len(sim.board.board) == 50
    assert len(sim.board.board[0]) == 50


def test_create_robot():
    sim = Simulation()
    sim.create_board()
    sim.create_robot("Alex", (0, 0), "N")
    assert sim.board.board[0][0] is not None


def test_create_dinosaur():
    sim = Simulation()
    sim.create_board()
    sim.create_dinosaur((1, 1))
    assert sim.board.board[1][1] is not None


def test_robot_instructions():
    sim = Simulation()
    sim.create_board()
    sim.create_robot("Maria", (3, 3), "N")
    robot = sim.board.board[3][3]
    sim.robot_instructions("Maria", "turn left")
    assert robot.direction == "W"

    sim.robot_instructions("Maria", "turn right")
    assert robot.direction == "N"

    sim.robot_instructions("Maria", "move backward")
    assert robot.row == 4

    sim.robot_instructions("Maria", "move forward")
    assert robot.row == 3

    sim.create_dinosaur((3, 4))
    assert sim.board.board[3][4] is not None

    sim.robot_instructions("Maria", "attack")
    assert sim.board.board[3][4] is None

