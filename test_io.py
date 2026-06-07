import unittest
from io_module import validate_board


class TestIO(unittest.TestCase):

    def test_valid_board(self):
        board = [[0 for _ in range(19)] for _ in range(19)]
        self.assertTrue(validate_board(board))

    def test_invalid_board_rows(self):
        board = [[0 for _ in range(19)] for _ in range(18)]
        self.assertFalse(validate_board(board))

    def test_invalid_board_cols(self):
        board = [[0 for _ in range(18)] for _ in range(19)]
        self.assertFalse(validate_board(board))

    def test_invalid_characters(self):
        board = [[0 for _ in range(19)] for _ in range(19)]
        board[5][5] = 5
        self.assertFalse(validate_board(board))


if __name__ == '__main__':
    unittest.main()