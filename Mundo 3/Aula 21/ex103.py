#Faça um programa que tenha uma funcao chamada ficha(), que receba dois parametros: o nome de um jogador e quantos gols ele marcou. O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.

def ficha (nome = '<desconhecido>', gols = 0):
    """
    Exibe a ficha de um jogador.

    :param nome: O nome do jogador (opcional).
    :param gols: O número de gols marcados (opcional).
    """

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nomejogador = input('Digite o nome do jogador: ').strip()
golsjogador = input('Numero de gols: ')

if golsjogador.isdigit():  #Quando você lê a entrada do usuário com input(), o valor recebido é sempre uma string, mesmo que o usuário digite um número. Para garantir que o valor digitado para "gols" seja realmente um número, usamos .isdigit() para verificar se a string contém apenas números.
    golsjogador = int(golsjogador)
else:
    golsjogador  = 0

if nomejogador == '':
    ficha(gols = golsjogador)
else:
    ficha(nomejogador, golsjogador)

