
def is_valid_game(board: list[list[int]]) -> bool:
    """
    Analisar um tabuleiro e dizer se o jogo é válido (mesmo que incompleto)
    ou não
    """

    # checar se linhas possuem repetições
    for linha in board:
        checklist = {}

        for coluna in linha:
            if coluna == 0:  # ignorar células vazias
                continue

            if coluna in checklist and checklist[coluna] == True:
                return False
            checklist[coluna] = True

    # checar se colunas possuem repetições
    index = 0
    for coluna in range(len(board)):
        checklist = {}

        for linha in board:
            valor = linha[index]

            if valor == 0:  # ignorar células vazias
                continue

            if valor in checklist and checklist[valor] == True:
                return False
            checklist[valor] = True

        index += 1

    return True




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


def solve(grid) :
    vazia = encontraLacunas(grid)
    if not vazia:
        return grid
    
    linha, coluna = vazia

    
    for num in range(1, 10):
        if possivel(grid,linha, coluna, num):
            grid[linha][coluna] = num
            if solve(grid):
                return grid
            else:
                grid[linha][coluna] = 0
                        
                        
                
    return None


def encontraLacunas(grid) -> tuple[int, int]:
    # Encontra a primeira célula vazia no tabuleiro
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None # type: ignore

