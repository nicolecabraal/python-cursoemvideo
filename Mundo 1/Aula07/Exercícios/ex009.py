#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. 

n = int(input('Digite um número inteiro:'))

print (f'A tabuada do número {n} é igual à:')
for i in range (1, 11):
    print(f'{n} x {i} = {n*i}')
