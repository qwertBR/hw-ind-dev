class Game:
    def __init__(self, field_size: int):
        self.size = field_size
        self.field = [
            ["." for row in range(self.size)] for column in range(self.size)
        ]  # l1 = [["."] * self.size] * self.size
        self.cur_turn = 0
        self.cur_move = [None, None]

    def print_board(self):
        for row in self.field:
            print(*row)
        print("\n")

    def is_win_position(self, check_x: int, check_y: int, placed_symbol: str) -> bool:
        x_diff = -1

        for y_diff in range(-1, 2):

            copy_x, copy_y = check_x, check_y
            required_cells_amount = min(self.size, 5)

            while (
                self.is_valid_coordinate(copy_x, copy_y)
                and self.field[copy_x][copy_y] == placed_symbol
            ):
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

    def is_free_cells_exists(self) -> bool:
        for row in self.field:
            for column in row:
                if column == ".":
                    return False
        return True

    def empty_cells_coordinates(self) -> list:
        assert not self.is_free_cells_exists()
        moves = []
        for row in range(self.size):
            for column in range(self.size):
                if self.field[row][column] == ".":
                    moves.append([row, column])
        return moves

    def move(self, input_sym: str):
        row, column = map(int, input("Type row and column. Example: 1 3 \n").split())

        # Minus 1 for indexation
        self.field[row - 1][column - 1] = input_sym

    def is_valid_coordinate(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size
