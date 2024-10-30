#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo da pessoa (M/F):').upper() #upper serve para garantir que tanto maiuscula quando minuscula sejam aceitas. 

while sexo != 'M' and sexo != 'F':
    print('Entrada inválida. Tente novamente:')
    sexo = input('Digite o sexo da pessoa (M/F):')

print(f'Sexo {sexo} registrado com sucesso.')

