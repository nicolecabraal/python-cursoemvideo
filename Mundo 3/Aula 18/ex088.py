#Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 

import random

def gerarpapalpites():
    jogos = []
    qtdjogos = int(input('Quantos jogos você deseja gerar?'))

    for _ in range(qtdjogos):
        jogo = random.sample(range(1,61), 6) #vai gerar 6 numeros unicos entre 1 e 60
        jogos.append(sorted(jogo)) #adiciona o jogo ordenado à lista de jogos

    return jogos

def exibirjogos(jogos):
    print('-=' *30)
    print('Jogos gerados: ')
    for i, jogo in enumerate(jogos, 1):
        print(f'Jogo {i}: {jogo}')

if __name__ == '__main__':
    palpites = gerarpapalpites() #gera os palpites
    exibirjogos(palpites) #exibe os jogos gerados 