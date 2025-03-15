def create_board(
    width: int, height: int, empty_space: str = "."
) -> dict[tuple[int, int], str]:
    board = {}
    for column_index in range(width):
        for row_index in range(height):
            board[(column_index, row_index)] = empty_space
    return board


def display_board(board): ...
