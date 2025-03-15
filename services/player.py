import sys

COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
EMPTY_SPACE = "."


def ask_player_to_move(
    player, board, height, width, lables=COLUMN_LABELS, empty_space=EMPTY_SPACE
):
    while True:
        print(f"Player {player}, enter a column number or QUIT:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("BYE!")
            sys.exit()

        if response not in lables:
            print("Enter a number from 1 to {}.".format(width))
            continue

        column_index = int(response) - 1

        if board[(column_index, 0)] != empty_space:
            print("That column is full, select another one.")
            continue

        for row_index in range(height - 1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)
