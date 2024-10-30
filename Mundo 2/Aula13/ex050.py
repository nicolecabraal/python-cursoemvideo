#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

soma = 0

for i in range(6):
    num = int(input(f'Digite o {i+1}° número:'))

    if num % 2 == 0:
        soma += num

print(f'A soma dos numeros pares é {soma}')

#No início do código, a linha soma = 0 é importante porque ela inicializa a variável soma com o valor zero. Isso garante que você tenha um ponto de partida correto para acumular a soma dos números pares.

#A expressão soma += numero é uma forma abreviada de escrever: soma = soma + numero
