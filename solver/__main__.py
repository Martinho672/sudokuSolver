import sys
import argparse
from solver import io, solver


def get_args():
    parser = argparse.ArgumentParser(
        prog="sudoku solver",
        description="Resolvedor de sudoku"
    )

    parser.add_argument("-i", "--input", dest="input")
    parser.add_argument("-o", "--output", dest="output")

    return parser.parse_args()


def main():
    args = get_args()

    if args.input != None:
        input_content = io.read_file(args.input)
    else:
        input_content = str(sys.stdin)

    if len(input_content) == 0:
        print("erro: nenhuma entrada")
        exit(-1)

    game = io.parse_text(input_content)
    result = solver.solve(game)
    output_content = io.format_game(result)

    if args.output != None:
        io.write_file(args.output, output_content)
    else:
        print(output_content)


try:
    main()
except Exception as error:
        print("erro:", error)
        exit(-1)
