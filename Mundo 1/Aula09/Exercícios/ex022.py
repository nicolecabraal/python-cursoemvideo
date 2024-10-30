#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (Sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo:')

maiuscula = nome.upper()
minuscula = nome.lower()
total = len(nome.replace(" ", " ")) #usado para remover os espaços
primeiro_nome = nome.split()[0]
num = len(primeiro_nome)


print(f'O seu nome em letras maíusculas fica assim: {maiuscula}')
print(f'O seu nome em letras minúsculas fica assim: {minuscula}')
print(f'O seu nome tem o total de {total} letras')
print(f'O seu primeiro nome tem {num} letras')




