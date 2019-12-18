# MTND
Implementação de Máquina de Turing Não Determinística (MTND)

# Descrição:

A entrada consiste da especificação de uma MTND e de um conjunto de palavras. A saída consiste de uma lista indicando ‘S’ caso a MTND reconheça a palavra em questão e ‘N’ caso contrário.

Entrada:

Na primeira linha, há uma lista de estados. Na segunda linha, há o alfabeto de entrada. Na terceira linha, há o alfabeto da fita. Na quarta linha, há o símbolo especial que limita a fita à esquerda. Na quinta linha, há o símbolo branco da fita. Na sexta linha, há o número total n de transições. Para cada uma das n linhas seguintes, há uma quíntupla <a, b, c, d, e> onde ‘a’ é o estado de origem, ‘b’ é o caractere a ser lido, ‘c’ é o estado de destino, ‘d’ é o símbolo a ser escrito e, por fim, ‘e’ é a direção, imóvel (I), esquerda (E) e direita (D). Em seguida, há um caractere informando o estado inicial. Em seguida, há uma lista de estados finais. Por fim, há uma lista de palavras de teste a ser reconhecida. Os itens da listas serão separados por espaço em branco. A palavra vazia é representada por *.

Saída:

O programa deve imprimir para cada palavra de teste ‘S’ se a MTND reconhece a palavra ou ‘N’ caso contrário.
