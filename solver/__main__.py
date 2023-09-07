import sys
import argparse
from solver import io

parser = argparse.ArgumentParser(
    prog="sudoku solver",
    description="Resolvedor de sudoku"
)

parser.add_argument("-i", "--input", dest="input")
parser.add_argument("-o", "--output", dest="output")

args = parser.parse_args()


if args.input != None:
    input_content = io.read_file(args.input)
else:
    input_content = str(sys.stdin)

if len(input_content) == 0:
    print("erro: nenhuma entrada")
    exit(-1)

game = io.parse_text(input_content)
output_content = str(game)

if args.output != None:
    print(output_content)
else:
    io.write_file(args.output, output_content)
