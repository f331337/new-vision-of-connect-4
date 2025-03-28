import sys

from services.board import create_board, display_board
from services.check_board import is_board_full, is_winner_exists
from services.player import ask_player_to_move

EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

BOARD_WIDTH, BOARD_HEIGHT = (7, 6)


def main():
    print("Hello from new CLI vision of connect 4!")

    board = create_board(width=BOARD_WIDTH, height=BOARD_HEIGHT)

    player_turn = PLAYER_X

    while True:
        display_board(board, width=BOARD_WIDTH, height=BOARD_HEIGHT)
        player_move = ask_player_to_move(
            player_turn, board, height=BOARD_HEIGHT, width=BOARD_WIDTH
        )
        board[player_move] = player_turn

        if is_winner_exists(player_turn, board, BOARD_WIDTH, BOARD_HEIGHT):
            display_board(board, width=BOARD_WIDTH, height=BOARD_HEIGHT)
            print(f"player {player_turn} won!")
            sys.exit()

        elif is_board_full(board, BOARD_HEIGHT, BOARD_WIDTH):
            display_board(board, width=BOARD_WIDTH, height=BOARD_HEIGHT)
            print("tie!")
            sys.exit()

        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


if __name__ == "__main__":
    main()
