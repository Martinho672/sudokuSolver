from pathlib import Path


def read_file(path: str) -> str:
    return Path(path).read_text(encoding="UTF-8")


def write_file(path: str, content: str):
    Path(path).write_text(content, encoding="UTF-8")


def parse_text(text: str) -> list[list[int]]:
    """
    Converter um tabuleiro em formato texto para uma matriz de valores
    """

    text = text.replace("\n", " ").replace("\r", " ")
    parts = text.split(" ")

    if len(parts) != 9 * 9:
        raise Exception("incorrect file format")

    result = []

    tmp = []
    for part in parts:
        if part.isdigit():
            tmp.append(int(part))
            if len(tmp) == 9:
                result.append(tmp)
                tmp = []
            continue

        raise Exception("invalid cell value")

    return result


def format_game(board: list[list[int]]) -> str:
    """
    Converter uma matriz de valores para um tabuleiro em formato texto
    """

    result = ""
    for i, linha in enumerate(board):
        if i > 0 and i % 3 == 0:
            result += "-" * 21 + "\n"

        for j, box in enumerate(linha):
            if j > 0 and j % 3 == 0:
                result += "| "
            result += str(box) + " "
        result = result[:-1] + "\n"

    return result
