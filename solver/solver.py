
def is_valid_game(board: list[list[int]]) -> bool:
    """
    Analisar um tabuleiro e dizer se o jogo é válido (mesmo que incompleto)
    ou não
    """

    return False


def possivel(grid, linha, coluna, num):
    # Retorna falso enquanto o numero passado n for possível de ser alocado a posição passada
    # Verificando linha
    for i in range(9):
        if grid[linha][i] == num:
            return False
    # Verificando coluna
    for i in range(9):
        if grid[i][coluna] == num:
            return False
    # Faz a verificação das "caixas" ou subgrupos do sudoku
    colunaAux = (coluna // 3) * 3
    linhaAux = (linha // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[linhaAux + i][colunaAux + j] == num:
                return False
    return True


def solve(grid: list[list[int]]) -> list[list[int]]:
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if possivel(grid, i, j, num):
                        grid[i][j] = num
                        solve(grid)
                        # retorna o valor inicial -> backtracking ?
                        grid[i][j] = 0
                return grid

    return grid
