#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados. 
#B) A soma dos valores da terceira coluna. 
#C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor: '))  

print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')  
    print()  

somapares = sum(matriz[1][c] for l in range(3) for c in range(3) if matriz[l][c] % 2 == 0)
somacolunatres = sum(matriz[l][2] for l in range(3))
maiorlinhadois = max(matriz[1])

print('-=' * 30)
print(f'A soma de todos os valores pares é: {somapares}')
print(f'A soma dos valores da terceira coluna é: {somacolunatres}')
print(f'O maior valor da segunda linha é: {maiorlinhadois}')