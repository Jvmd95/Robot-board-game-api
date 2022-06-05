import pytest
from src.robot import Robot


def test_init_ok():
    robot = Robot("Izabella", 0, 1, "N")
    assert robot.name == "Izabella"
    assert robot.row == 0
    assert robot.column == 1
    assert robot.direction == "N"


def test_turn_left():
    robot = Robot("Izabella", 0, 1, "N")
    robot.turn_left()
    assert robot.direction == "W"


def test_turn_right():
    robot = Robot("Izabella", 0, 1, "N")
    robot.turn_right()
    assert robot.direction == "E"
