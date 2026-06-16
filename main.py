from io_module import read_input, write_output
from renju_core import find_winner


def main():
    file_path = "input.txt"
    boards = read_input(file_path)

    if not boards:
        print("Немає даних для обробки. Перевірте файл input.txt")
        return

    results = []
    for board in boards:
        # find_winner має повертати кортеж (переможець, рядок, стовпець) або (0,)
        result = find_winner(board)
        results.append(result)

    # 3. Записуємо результати у файл
    write_output(results, "output.txt")
    print(f"Гру завершено! Оброблено {len(boards)} тест-кейсів. Результати у файлі output.txt")


if __name__ == "__main__":
    main()