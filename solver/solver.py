# import numpy

grid = [
    [0, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 1, 0, 7, 0, 5, 0, 2, 0],
    [4, 0, 0, 0, 9, 0, 0, 0, 7],
    [0, 4, 9, 0, 0, 0, 7, 3, 0],
    [8, 0, 1, 0, 3, 0, 4, 0, 9],
    [0, 3, 6, 0, 0, 0, 2, 1, 0],
    [2, 0, 0, 0, 8, 0, 0, 0, 4],
    [0, 8, 0, 9, 0, 2, 0, 6, 0],
    [0, 0, 7, 0, 0, 0, 8, 0, 0]
]


def possivel(grid, linha, coluna, num):
    for i in range(9):
        if grid[linha][i] == num:
            return False
    for i in range(9):
        if grid[i][coluna] == num:
            return False
    colunaAux = (coluna // 3) * 3
    linhaAux = (linha // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[linhaAux + i][colunaAux + j] == num:
                return False
    return True


# print("entrada = \n", numpy.matrix(grid))
print(possivel(grid, 0, 0, 3))


def solve(grid):
    pass
