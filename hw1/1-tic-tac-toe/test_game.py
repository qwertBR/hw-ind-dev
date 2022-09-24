from game import Game
import pytest


@pytest.fixture
def empty_game():
    return Game()


@pytest.fixture
def game():
    return Game(3)


def test_default_game(game):
    assert game.field == [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


def test_move(game):
    assert game.cur_move == [None, None]


def test_size(game):
    assert len(game.field) == len(game.field[0])
