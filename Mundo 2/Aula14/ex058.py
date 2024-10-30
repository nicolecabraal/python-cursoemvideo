#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

num = random.randint(0, 10)

palpites = 0
acertou = False

print('Tente adivinhar o número que o computador escolheu, entre 0 e 10.')

while not acertou:
    num_usuario = int(input("Seu palpite: "))
    palpites += 1
    
    if num_usuario == num:
        acertou = True
        print(f"Parabéns! Você acertou o número {num} em {palpites} tentativas.")
    else:
        print("Errou! Tente novamente.")