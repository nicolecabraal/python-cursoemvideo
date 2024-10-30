#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite o seu nome completo:')

silva = nome.find('Silva')

if silva != -1:
    print("Você possui 'Silva' no seu nome!")
else:
    print("Você NÃO POSSUI 'Silva' no seu nome")