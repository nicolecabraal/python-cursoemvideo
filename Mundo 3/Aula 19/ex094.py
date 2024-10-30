#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final mostre: 
#A) Quantas pessoas foram cadastradas
#B) A media de idade do grupo
#C) Uma lista com todas as mulheres. 
#D) Uma lista com todas as pessoas com idade acima da média

pessoas = []
mulheres = []
somaidades = []

while True:
    pessoa = {}

    pessoa ['nome'] = input('Nome:')
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()
    while pessoa ['sexo'] not in ['M/F']:
        pessoa['sexo'] = input('ERRO. Por favor, digente apenas M ou F: ')
    
    pessoa ['idade'] = int(input('Idade:'))
    somaidades += pessoa ['idade']
    pessoas.append(pessoa)


    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('ERRO! Responda apenas S ou N: ').strip().upper()
    if continuar == 'N':
        break

totalpessoas = len(pessoas)
mediaidade = somaidades / totalpessoas
acimamedia = [p for p in pessoas if p['idade'] > mediaidade]

print('-=' * 30)
print(f'A) Ao todo, temos {totalpessoas} pessoas cadastradas.')
print(f'B) A média de idade do grupo é de {mediaidade:.2f} anos.')
print('C) As mulheres cadastradas foram: ', ', '.join(mulheres))
print('D) Lista das pessoas com idade acima da média:')

for p in acimamedia:
    print(f'    Nome = {p["nome"]}; Idade = {p["idade"]}')