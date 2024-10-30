#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))  #atribui o valor a posição correta na matriz

#formatando a matriz
print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')  #formatação para centralizar os valores em 5 espaços
    print()  #quebra de linha a cada nova linha da matriz

