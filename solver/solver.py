import numpy


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
    #Retorna falso enquanto o numero passado n for possível de ser alocado a posição passada
    #Verificando linha
    for i in range(9):
        if grid[linha][i] == num:
            return False
    #Verificando coluna
    for i in range(9):
        if grid[i][coluna] == num:
            return False
    #Faz a verificação das "caixas" ou subgrupos do sudoku
    colunaAux = (coluna // 3) * 3 
    linhaAux = (linha // 3) * 3 
    for i in range(3):
        for j in range(3):
            if grid[linhaAux + i][colunaAux + j] == num:
                return False
    return True


# print("entrada = \n", numpy.matrix(grid))
#print(possivel(grid, 0, 0, 3))


def solver(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if possivel(grid, i, j, num):
                        grid[i][j] = num
                        solver(grid)
                        grid[i][j] = 0 #retorna o valor inicial -> backtracking ?
                return
    print("saida = \n", numpy.matrix(grid))
    pass

solver(grid[:])