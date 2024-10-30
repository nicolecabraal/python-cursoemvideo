#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa em reais: R$'))
salario = float(input('Digite o valor do seu salário em reais: R$'))
anos = int(input('Em quantos anos você irá pagar a casa?'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:2f} em {anos} anos, a prestação será de R${prestação:2f}')

if prestação <= minimo:
    print('Parabéns! O empréstimo pode ser concedido!')
else:
    print('Empréstimo negado.')