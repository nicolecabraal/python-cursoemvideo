#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
#Ate 9 anos: MIRIM
#Ate 14 anos: INFANTIL
#Ate 19 anos: JUNIOR
#Ate 20 anos: SENIOR
#Acima de 20: MASTER

from datetime import date


nascimento = int(input('Digite o ano de nascimento do atleta:'))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL.')
elif idade <=19:
    print('Categoria JUNIOR.')
elif idade <=25:
    print('Categoria SENIOR.')
else:
    print('Categoria MASTER.')
