#Crie um programa que faça o computador jogar jokenpo com voce

import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(opcoes)
print("Suas opções: [0] Pedra, [1] Papel, [2] Tesoura")
jogador = int(input("Qual é a sua jogada? "))


if jogador >= 0 and jogador <= 2:
    print(f"Você jogou {opcoes[jogador]}")
    print(f"O computador jogou {computador}")
    
    
    if opcoes[jogador] == computador:
        print("Empate!")
    elif (opcoes[jogador] == 'Pedra' and computador == 'Tesoura') or \
         (opcoes[jogador] == 'Papel' and computador == 'Pedra') or \
         (opcoes[jogador] == 'Tesoura' and computador == 'Papel'):
        print("Você venceu!")
    else:
        print("O computador venceu!")
else:
    print("Jogada inválida! Escolha 0, 1 ou 2.")
