import pytest
from src.dinosaur import Dinosaur


def test_init_ok():
    dino = Dinosaur(0, 1)
    assert dino.row == 0
    assert dino.column == 1
