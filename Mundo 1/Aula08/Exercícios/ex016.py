#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
#Exemplo:
#Digite um número:
#O numéro {num} tem a parte inteira:


import math 

real = float(input('Digite um número real:'))
int = math.trunc(real)
print(f'A porção inteira de {real} é igual à: {int}')
