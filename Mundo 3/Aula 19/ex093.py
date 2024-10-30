#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols_partidas = []

jogador ['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i +1}?'))
    gols_partidas.append(gols)

jogador ['gols'] = gols_partidas[:]
jogador['total_gols'] = sum(gols_partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, gols in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {gols} gols.')

print(f'Foi um total de {jogador["total_gols"]} gols no campeonato.')