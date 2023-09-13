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
    if not solver.is_valid_game(game):
        print("erro: a entrada não apresenta um jogo válido")
        exit(-1)
 
    result = solver.solve(game)
    if result is None:
        print("erro: nenhum resultado encontrado")
        exit(-1)

    if not solver.is_valid_game(result):
        print("erro: a entrada não apresenta um jogo válido")
        exit(-1)
    
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
