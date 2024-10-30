#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 

import random

num = random.randint(0,5)

num_usuario = int(input("Tente adivinhar o npumero que o computador escolheu (entre 0 e 5): "))

if num_usuario == num:
    print('Parabéns! Você acertou')
else:
    print(f'Errou. O número escolhido pelo computador foi {num}')