#Faça um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

vitorias = 0

while True:
    escolha = input('Você escolhe par ou ímpar? [P/I]:').strip().upper()
    jogador =int(input('Digite um número:'))
    computador = random.randint(0,10)
    total = jogador + computador

    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end=' ')

    if total % 2 == 0:
        print('Deu PAR')
        resultado = 'P'
    else:
        print('Deu IMPAR')
        resultado = 'I'
    
    if escolha == resultado:
        print('Você VENCEU!')
        vitorias += 1
    else:
        print('Você perdeu. :( ', end = ' ')
        break
print(f'GAME OVER. Você teve um total de {vitorias} vitórias consecutivas.')