#Crie um programa que leia nome, ano de nascimento e a carteira de trabalho e cadastre-os (com idade) em um dicionario. se por acaso a CTPS for diferente de ZERO, o dicionario receberá tambem o ano de contratacao e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar. 

from datetime import datetime

trabalhador = {}

trabalhador ['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
trabalhador ['idade'] = datetime.now().year - nascimento
trabalhador ['ctps'] = int(input('Cateira de trabalho (0 se não tem): '))

if trabalhador ['ctps'] != 0:
    trabalhador ['anocontratacao'] = int(input('Ano de contratação: '))
    trabalhador ['salario'] = float(input('Salario: R$'))

    trabalhador ['contribuicao'] = datetime.now().year - trabalhador ['anocontratacao']
    trabalhador ['aposentadoria'] = trabalhador ['idade'] + (35 - trabalhador['contribuicao'])

print('-=' * 30)

for chave, valor in trabalhador.items():
    print(f'{chave.capitalize()}: {valor}')