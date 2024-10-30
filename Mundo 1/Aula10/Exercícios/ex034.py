#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o seu salário:'))


if salario > 1250:
    aumento1 = salario *0.10
    novosalario1 = salario + aumento1
    print(f'Parabéns! Você recebeu um aumento de {aumento1} e seu novo salário é igual à {novosalario1}')
else:
    aumento2 = salario *0.15
    novosalario2 = salario + aumento2
    print(f'Parabéns! Você recebeu um aumento de {aumento2} o seu novo salário é igual à {novosalario2}')