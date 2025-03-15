def is_winner_exists(player, board, width, height):
    for column_index in range(width - 3):
        for row_index in range(height):
            # -> horizontal :
            player_sign_1 = board[(column_index, row_index)]
            player_sign_2 = board[(column_index + 1, row_index)]
            player_sign_3 = board[(column_index + 2, row_index)]
            player_sign_4 = board[(column_index + 3, row_index)]
            if (
                player_sign_1
                == player_sign_2
                == player_sign_3
                == player_sign_4
                == player
            ):
                return True

    for column_index in range(width):
        for row_index in range(height - 3):
            # vertical down:
            player_sign_1 = board[(column_index, row_index)]
            player_sign_2 = board[(column_index, row_index + 1)]
            player_sign_3 = board[(column_index, row_index + 2)]
            player_sign_4 = board[(column_index, row_index + 3)]
            if (
                player_sign_1
                == player_sign_2
                == player_sign_3
                == player_sign_4
                == player
            ):
                return True

    for column_index in range(width - 3):
        for row_index in range(height - 3):
            # diag right down
            player_sign_1 = board[(column_index, row_index)]
            player_sign_2 = board[(column_index + 1, row_index + 1)]
            player_sign_3 = board[(column_index + 2, row_index + 2)]
            player_sign_4 = board[(column_index + 3, row_index + 3)]
            if (
                player_sign_1
                == player_sign_2
                == player_sign_3
                == player_sign_4
                == player
            ):
                return True

            # diag left down:
            player_sign_1 = board[(column_index + 3, row_index)]
            player_sign_2 = board[(column_index + 2, row_index + 1)]
            player_sign_3 = board[(column_index + 1, row_index + 2)]
            player_sign_4 = board[(column_index, row_index + 3)]
            if (
                player_sign_1
                == player_sign_2
                == player_sign_3
                == player_sign_4
                == player
            ):
                return True
    return False


def is_board_full(board, height, width, empty_space="."):
    for row_index in range(height):
        for column_index in range(width):
            if board[(column_index, row_index)] == empty_space:
                return False
    return True
