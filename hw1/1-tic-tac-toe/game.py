from ctypes import sizeof


# TURNS = {"COMPUTER_TURN": "X", "PLAYER_TURN": "0"}


class Game:
    def __init__(self, field_size: int, turn):
        self.size = field_size
        self.board = self.board()
        self.cur_turn = turn

    def print_board(self):
        for row in self.board:
            print(*row)

    def board(self) -> list:
        field = [["."] * self.size] * self.size
        return field

    def is_win_position(self, check_x: int, check_y: int, placed_symbol: str) -> bool:
        x_diff = -1

        for y_diff in range(-1, 2):

            copy_x, copy_y = check_x, check_y
            required_cells_amount = min(self.size, 5)

            while self.board[copy_x][copy_y] == placed_symbol:
                copy_x += x_diff
                copy_y += y_diff
                required_cells_amount -= 1

                if required_cells_amount == 0:
                    return True

        return False

    def is_gewonnen(self, placed_symbol: str) -> bool:
        for row in range(self.size):
            for column in range(self.size):
                if self.is_win_position(row, column, placed_symbol):
                    return True
        return False

    def is_game_finished(self) -> bool:
        for row in self.board:
            for column in row:
                if column == ".":
                    return False
        return True

    def moves_variants(self):
        moves = []
        for row in range(self.size):
            for column in range(self.size):
                if self.board[row][column] == ".":
                    moves.append([row, column])
        return moves

    def move(self, input_sym: str):
        row, column = map(int, input("Type row and kolonky. Example: 1 3 \n").split())

        # Minus 1 for indexation
        self.board[row - 1][column - 1] = input_sym
