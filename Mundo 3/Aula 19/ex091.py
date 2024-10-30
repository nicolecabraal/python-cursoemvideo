#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 

import random
from operator import itemgetter

jogadores = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6),
}

print('Resultados dos jogadores: ')
for jogador, resultado in jogadores.items():
    print(f'{jogador} tirou {resultado} no dado')


ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('Ranking dos jogadores:')
for i, (jogador, resultado) in enumerate(ranking, 1):
    print(f'{i}º lugar: {jogador} com {resultado} no dado')