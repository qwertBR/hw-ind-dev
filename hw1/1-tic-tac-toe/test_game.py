from game import Game
import pytest
import mock


@pytest.fixture
def empty_game():
    return Game()


@pytest.fixture
def game():
    return Game(3)


def test_default_field(game: Game):
    assert game.field == [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


def test_default_move(game: Game):
    assert game.cur_move == [None, None]


def test_size(game: Game):
    assert len(game.field) == len(game.field[0])


@pytest.mark.parametrize(
    "field, result",
    [
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], False),
        ([["O", "X", "X"], ["X", "O", "X"], ["O", "X", "O"]], True),
        ([[".", "X", "."], [".", ".", "."], [".", "O", "X"]], False),
    ],
)
def test_is_free_cells_exists(game: Game, field: list, result: bool):
    game.field = field
    assert game.is_free_cells_exists() == result


@pytest.mark.parametrize(
    "field, coords, sym, result",
    [
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], [1, 1], "X", False),
        ([[".", "X", "."], [".", "X", "."], [".", "X", "."]], [2, 1], "X", True),
        ([["O", ".", "."], [".", "O", "."], [".", ".", "O"]], [2, 2], "O", True),
        ([["O", ".", "."], ["X", "X", "."], [".", ".", "O"]], [2, 2], "O", False),
    ],
)
def test_is_win_position(game: Game, field: list, coords: list, sym: str, result: bool):
    game.field = field
    assert game.is_win_position(coords[0], coords[1], sym) == result


@pytest.mark.parametrize(
    "input_symbol, result",
    [("X", [["X", ".", "."], [".", ".", "."], [".", ".", "."]])],
)
@mock.patch("game.input", return_value="1 1")
def test_move(mock_input: str, game: Game, input_symbol: str, result: list):
    game.move(input_symbol)
    mock_input.return_value
    assert game.field == result
