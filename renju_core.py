from __future__ import annotations
from enum import Enum

class Players(Enum):
    BLACK = 1
    WHITE = 2

BOARD_SIZE = 19
WINNING_LENGTH = 5

def create_board() -> list[list[int]]:
    return [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def clear_board(board: list[list[int]]) -> None:
    """
    Clears board. (for tests)
    """
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            board[row][col] = 0


def fill_board(board: list[list[int]], lines: list[str]) -> None:
    """
    Fills board.
    """
    for row_idx, line in enumerate(lines):
        values = line.split()
        for col_idx, val in enumerate(values):
            board[row_idx][col_idx] = int(val)


DIRECTIONS = [
    (0, 1),   # horizontal
    (1, 0),   # vertical
    (1, 1),   # main diagonal
    (1, -1),  # lateral diagonal
]


def _count_consecutive(
    board: list[list[int]],
    start_row: int,
    start_col: int,
    delta_row: int,
    delta_col: int,
    player: int,
) -> int:
    """
    Counts the number of consecutive stones for the `player`,
    starting from the cell (start_row, start_col) in the direction (dr, dc).
    """
    count = 0
    row, col = start_row, start_col
    while 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == player:
        count += 1
        row += delta_row
        col += delta_col
    return count


def _is_start_of_sequence(
    board: list[list[int]],
    row: int,
    col: int,
    delta_row: int,
    delta_col: int,
    player: int,
) -> bool:
    """
    Checks that the cell (row, col) is the start of a new sequence
    (i.e., the previous cell in the opposite direction is not a stone of the same player).
    """
    prev_r = row - delta_row
    prev_c = col - delta_col
    if 0 <= prev_r < BOARD_SIZE and 0 <= prev_c < BOARD_SIZE:
        return board[prev_r][prev_c] != player
    return True  # вийшли за межі — це початок


def find_winner(board: list[list[int]]) -> tuple[int, int, int] | tuple[int]:
    """
    Scanning board for 5 connected nodes
        Returns:
        (player, row, col) — if a winner is found,
        where (row, col) are the 1-indexed coordinates of the leftmost or topmost cell.
        (0,) — if there is no winner yet.
    """
    for player in (Players.BLACK, Players.WHITE):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] != player:
                    continue
                for dr, dc in DIRECTIONS:
                    if not _is_start_of_sequence(board, row, col, dr, dc, player):
                        continue
                    length = _count_consecutive(board, row, col, dr, dc, player)
                    if length == WINNING_LENGTH:
                        # Перетворюємо у 1-індексовані координати
                        return (player, row + 1, col + 1)
    return (0,)

def check_board(board: list[list[int]]) -> tuple:
    return find_winner(board)