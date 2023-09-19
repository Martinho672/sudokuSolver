# Relatório de Desenvolvimento - Código Sudoku

**Fernando Martinho Nascimento & Lucas Guimarães Bernardes**

Este relatório busca descrever de forma simplista a implementação de algumas funções e os desafios encontrados durante seu desenvolvimento.

## Função `is_valid_game`

A primeira função, `is_valid_game`, tem como objetivo analisar um tabuleiro de entrada e determinar se ele é válido, ou seja se ele já não possui células conflitantes ou um formato inesperado de arquivo. O principal desafio aqui foi verificar se linhas e colunas não continham números repetidos. Para isso, foi necessário manter um controle das ocorrências dos números em cada linha e coluna. A lógica de iteração sobre o tabuleiro, ignorando células vazias (com valor 0), já que essas devem ser preenchidas durante a resolução do tabuleiro. A função retornará `True` se o tabuleiro for válido e `False` se houver repetições.

## Função `possivel`

A função `possivel` verifica se é possível alocar um número em uma posição específica do tabuleiro de entrada. O código faz três verificações: se o número já existe na mesma linha, na mesma coluna e na mesma "caixa" (um dos subgrupos de 3x3 do Sudoku). Esta função é essencial para a resolução do Sudoku. 
O principal desafio foi garantir que todas as três verificações fossem implementadas corretamente e retornassem os resultados esperados.

## Função `solve`

A função `solve` é responsável por resolver o tabuleiro de Sudoku usando a abordagem de força bruta, preenchendo as células vazias com números válidos até que o tabuleiro esteja completo ou seja determinado que a configuração atual não leva a uma solução válida. O desafio aqui foi implementar a recursão corretamente e garantir que a função tentasse todas as possibilidades até encontrar uma solução ou determinar que não há solução possível e que fosse feito o Baktracking em caso de erro. 

## Função `encontraLacunas`

A função `encontraLacunas` encontra a primeira célula vazia (com valor 0) no tabuleiro de Sudoku. Esta função é utilizada pela função `solve` para encontrar a próxima célula vazia a ser preenchida. O desafio aqui foi escrever um loop duplo para iterar sobre todas as células do tabuleiro e retornar a posição da primeira célula vazia encontrada. Esta acabou sendo uma das últimas funções implementadas, já que no começo acreditavamos que apenas a função de `possibilidade` já seria o sufiente juntamente com a função `solve` para resolver o problema, no entanto muitas células acabavam não sendo preenchidas ou tinham seu valor setado para 0 em algum momento das iterações.

## Testes
Foram realizados diferentes testes com os arquivos disponibilizados pelo professor, e conferidos os resultados, no entando nosso código não lê arquivos que não possuem o formato pré definido como podem ser encontrados na pasta tests como por exemplo o `game1.txt`.


##### EXIT
Em resumo, o desenvolvimento deste código Solver envolveu a utilização das técnicas estudadas em sala de aula durante as últimas semanas e foi fundamental para fixar os conteúdos absorvidos. 
