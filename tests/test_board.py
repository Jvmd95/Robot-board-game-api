import pytest
from src.board import Board


def test_init_ok():
    board = Board()
    assert len(board.board) == 50
    assert len(board.board[0]) == 50
