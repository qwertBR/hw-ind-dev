from math import factorial
from game import Game


def minimax_algo(game: Game, depth: int) -> bool:
    if game.is_gewonnen("X") or game.is_gewonnen("O") or game.is_game_finished():
        if game.is_win("X"):
            return depth - 10
        if game.is_win("O"):
            return 10 - depth
        return 0

    final_score = -10e7

    cur_move = game.possible_moves()[0]

    it = game.possible_moves()
    for i in it():

        cur_move = game.cur_turn


def run(size: int, tree_depth: int) -> int:
    game_unit = Game(size, "X")

    game_unit.print_board()

    while not game_unit.is_game_finished():
        game_unit.move("X")
        game_unit.print_board()

        if game_unit.is_gewonnen("X"):
            return 0

        minimax_algo(game_unit, tree_depth)


if __name__ == "__main__":

    n = int(input("Enter n to define field size (n X n"))
    x_or_o = input("Select your side 1 - X, 2 - 0")

    tree_depth = 0

    if n > 3:
        tree_depth = 5

    else:
        tree_depth = factorial(9)

    run(n, tree_depth)
