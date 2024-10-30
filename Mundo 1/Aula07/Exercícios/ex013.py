#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento. 

print ('Vamos calcular como seria se você tivesse 15% de aumento?')

salario = float(input('Qual o valor do seu salário?'))

aumento = salario * 0.15

novo_salario = salario + aumento

print (f'Com aumento de 15%, seu novo salário é: R${novo_salario:.2f}.')
