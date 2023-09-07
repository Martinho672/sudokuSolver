from pathlib import Path
from solver import GameBoard


def read_file(path: str) -> str:
    return Path(path).read_text(encoding="UTF-8")


def write_file(path: str, content: str):
    Path(path).write_text(content, encoding="UTF-8")


def parse_text(text: str) -> list[list[int]]:
    """
    Converter um tabuleiro em formato texto para uma lista de valores
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


def is_valid_game(board: GameBoard) -> bool:
    """
    Analisar um tabuleiro e dizer se o jogo é válido (mesmo que incompleto)
    ou não
    """

    return False
