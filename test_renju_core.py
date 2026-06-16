"""
Тести для модуля renju_core (Студент 1).
Запуск: python -m pytest test_renju_core.py -v
     або: python test_renju_core.py
"""
from __future__ import annotations
import unittest
from renju_core import create_board, clear_board, check_board


class TestRenjuCore(unittest.TestCase):

    def setUp(self):
        self.board = create_board()

    def test_horizontal_black_wins(self):
        for c in range(5):
            self.board[0][c] = 1
        self.assertEqual(check_board(self.board), (1, 1, 1))

    def test_six_in_a_row_no_win(self):
        for c in range(6):
            self.board[0][c] = 1
        self.assertEqual(check_board(self.board), (0,))

    def test_vertical_white_wins(self):
        for r in range(5):
            self.board[r][3] = 2
        self.assertEqual(check_board(self.board), (2, 1, 4))

    def test_main_diagonal_black_wins(self):
        for i in range(5):
            self.board[2 + i][2 + i] = 1
        self.assertEqual(check_board(self.board), (1, 3, 3))

    def test_anti_diagonal_white_wins(self):
        for i in range(5):
            self.board[i][4 - i] = 2
        self.assertEqual(check_board(self.board), (2, 1, 5))

    def test_empty_board_no_winner(self):
        self.assertEqual(check_board(self.board), (0,))

    def test_clear_board_resets_state(self):
        for c in range(5):
            self.board[0][c] = 1
        clear_board(self.board)
        self.assertEqual(check_board(self.board), (0,))

    def test_seven_in_a_row_no_win(self):
        for c in range(7):
            self.board[5][c] = 2
        self.assertEqual(check_board(self.board), (0,))

    def test_win_at_board_edge(self):
        for c in range(5):
            self.board[18][c] = 1
        self.assertEqual(check_board(self.board), (1, 19, 1))

    def test_four_in_a_row_no_win(self):
        for c in range(4):
            self.board[0][c] = 1
        self.assertEqual(check_board(self.board), (0,))


if __name__ == "__main__":
    unittest.main(verbosity=2)