#crie um programa com uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes

from datetime import datetime

def voto(anonasc):
    anoatual = datetime.now().year
    idade = anoatual - anonasc

    if idade < 16:
        return 'NEGADO'
    elif 16<= idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else: 
        return 'OBRIGATÓRIO'


nascimento = int(input('Digite seu ano de nascimento: '))
print(f'Para quem em {nascimento}, o voto é: {voto(nascimento)}')

