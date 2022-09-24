from game import Game

PLAYER = "X"
COMPUTER = "O"


def minimax_algo(game: Game, depth: int) -> int:  # TODO INPUT

    if game.is_free_cells_exists():
        if game.is_gewonnen(COMPUTER):
            return 10 - depth
        if game.is_gewonnen(PLAYER):
            return -10 + depth
        return 0

    final_score = None

    empty_cells_coordinates = game.empty_cells_coordinates()
    for cell_coordinate in empty_cells_coordinates:

        current_turn = game.cur_turn

        row, column = cell_coordinate[0], cell_coordinate[1]

        if game.cur_turn == 0:

            game.field[row][column] = PLAYER

        else:
            game.field[row][column] = COMPUTER

        game.cur_turn = 1 - game.cur_turn

        score = minimax_algo(game, depth)

        if current_turn == 1:
            if final_score is None or score > final_score:
                final_score, cur_move = score, cell_coordinate

        elif final_score is None or score < final_score:
            final_score, cur_move = score, cell_coordinate

        game.field[row][column] = "."
        game.cur_turn = current_turn

    game.cur_move = cur_move
    return final_score


def run(size: int, depth: int) -> int:

    game_unit = Game(size)

    game_unit.print_board()

    while not game_unit.is_free_cells_exists():
        game_unit.move(PLAYER)
        game_unit.print_board()

        if game_unit.is_gewonnen(PLAYER):
            return 0

        print("tarting minimax\n")

        minimax_algo(game_unit, depth)  # TODO: call

        print("Next turn\n")

        row, column = game_unit.cur_move[0], game_unit.cur_move[1]

        game_unit.field[row][column] = COMPUTER
        game_unit.print_board()

        if game_unit.is_gewonnen(COMPUTER):
            return 1

    return 2


if __name__ == "__main__":

    n = int(input("Enter n to define field size (n X n)  "))
    x_or_o = int(input("Select your side 1 - X, 2 - 0  "))

    if x_or_o == 2:
        PLAYER = "O"
        COMPUTER = "X"

    tree_depth = 5

    winner = run(n, tree_depth)

    if winner == 0:
        print("User won")
    elif winner == 1:
        print("Computer won")
    else:
        print("Draw")
