from services.board import create_board


def test_create_board():
    board = create_board(2, 2)

    expected_board = {(0, 0): ".", (0, 1): ".", (1, 0): ".", (1, 1): "."}
    assert board == expected_board
