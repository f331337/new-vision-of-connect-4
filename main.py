from services import create_board, display_board


EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

BOARD_WIDTH, BOARD_HEIGHT = (7, 6)


def main():
    print("Hello from new CLI vision of connect 4!")

    board = create_board(width=BOARD_WIDTH, height=BOARD_HEIGHT)
    display_board(board, width=BOARD_WIDTH, height=BOARD_HEIGHT)


if __name__ == "__main__":
    main()
