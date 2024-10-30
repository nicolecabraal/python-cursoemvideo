#Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteudo da estrutura na tela.

aluno = {}

aluno['nome'] = input('Digite o nome do aluno:')
aluno ['media'] = float(input(f'Digite a média do aluno(a) {aluno["nome"]}: '))

if aluno ['media'] >=7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('-=' *30)

for chave, valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')