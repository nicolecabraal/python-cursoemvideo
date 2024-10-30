#Faça um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio() e somaPar(). A primeira funcao vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior. 

import random

numeros = []  

def sorteio():
    print("Sorteando 5 números para a lista:")
    for _ in range(5):
        num = random.randint(1, 100)  
        numeros.append(num)
        print(num, end=' ')
    print('\n')

def somaPar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:  
            soma += num
    print(f'A soma dos números pares sorteados é: {soma}')


sorteio()
somaPar()
