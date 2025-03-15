def create_board(
    width: int, height: int, empty_space: str = "."
) -> dict[tuple[int, int], str]:
    board = {}
    for column_index in range(width):
        for row_index in range(height):
            board[(column_index, row_index)] = empty_space
    return board


def display_board(board, height: int, width: int) -> list:
    board_to_display = []
    for row_index in range(height):
        for column_index in range(width):
            board_to_display.append(board[(column_index, row_index)])
    
    # Make it resizeble 
    print(
        """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*board_to_display)
    )
