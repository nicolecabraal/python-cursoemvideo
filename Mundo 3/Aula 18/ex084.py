#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quandas pessoas foram cadastradas. 
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

pessoas =[]
dados = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear() 

    continuar = input('Deseja continuar? (s/n): ').strip().lower()
    if continuar == 'n':
        break

total = len(pessoas)
pesos = [p[1] for p in pessoas]
pesomax = max(peso)
pesomin = min(peso)

pesadas = [p[0] for p in pessoas if p[1] == pesomax]
leves = [p[0] for p in pessoas if p[1] == pesomin]

print(f'O total de pessoas cadastradas é igual à: {total}')
print(f'As pessoas mais pesadas são {pesadas} com {pesomax} kg.')
print(f'As pessoas mais leves são {leves} com {pesomin} kg.')