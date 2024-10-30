#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 

jogadores = []


while True:
    jogador = {}  
    partidas = []  

    
    jogador['nome'] = input('Nome do jogador: ')
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    
    for i in range(total_partidas):
        gols = int(input(f'    Quantos gols na partida {i+1}? '))
        partidas.append(gols)

    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    
    jogadores.append(jogador)

    
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('ERRO! Responda apenas S ou N: ').strip().upper()

    if continuar == 'N':
        break


print('-=' * 30)
print('cod ', end='')
print(f'{"Nome":<15}{"Gols":<20}{"Total":>5}')
print('-' * 40)

for i, jogador in enumerate(jogadores):
    print(f'{i:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<5}')


while True:
    print('-' * 40)
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    if opcao >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {opcao}!')
    else:
        jogador = jogadores[opcao]
        print(f' -- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, gols in enumerate(jogador['gols']):
            print(f'    No jogo {i+1} fez {gols} gols.')
print('<< VOLTE SEMPRE >>')
