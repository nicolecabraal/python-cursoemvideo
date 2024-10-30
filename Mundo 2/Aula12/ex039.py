#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar 
#Se ja passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

atual = date.today().year
nascimento = int(input('Em que ano você nasceu?'))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade <18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
elif idade > 18:
    saldo2 = idade - 18
    print(f'Você já deveria ter se alistado há {saldo2} anos')