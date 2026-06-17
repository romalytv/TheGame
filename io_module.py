import os

BOARD_SIZE = 19

def read_input(file_path):
    """Читає вхідний файл та парсить тест-кейси[cite: 61, 62]."""
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не знайдено.")
        return []

    test_cases = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

        if not lines:
            return test_cases

        num_cases = int(lines[0])
        idx = 1

        for _ in range(num_cases):
            board = []
            for _ in range(BOARD_SIZE):
                row = list(map(int, lines[idx].split()))
                board.append(row)
                idx += 1
            test_cases.append(board)

    return test_cases


def validate_board(board):
    """Перевіряє розмірність матриці 19x19 та коректність значень[cite: 62, 63]."""
    if len(board) != BOARD_SIZE:
        return False
    for row in board:
        if len(row) != BOARD_SIZE:
            return False
        for cell in row:
            if cell not in (0, 1, 2):
                return False
    return True


def write_output(results, file_path="output.txt"):
    """
    Записує результати у файл.
    У першому рядку - переможець (1, 2 або 0)[cite: 66].
    У другому - координати крайнього лівого або найвищого каменя[cite: 67, 68].
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        for res in results:
            winner = res[0]
            f.write(f"{winner}\n")
            if winner != 0 and len(res) == 3:
                f.write(f"{res[1]} {res[2]}\n")