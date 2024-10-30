#Crie um programa que leia o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#A) Qual o total gasto na compra.
#B) Quantos produtos custam mais de R$1000,00
#C) Qual o nome do produto mais barato

total = 0
acima1000 = 0
min = float('inf') #inicializa com infinito pra poder encontrar o menor
barato = ''

while True:
    produto = input('Digite o nome do produto:')
    preco = float(input('Digite o preço do produto escolhido: R$'))

    total += preco

    if preco > 1000:
        acima1000 += 1
    
    if preco < min:
        min = preco
        barato = produto
    
    continuar = input('Deseja continuar? [S/N]').strip().upper()
    if continuar != 'S':
        break

print(f'A) Total gasto na compra: R$ {total:.2f}')
print(f'B) Quantidade de produtos acima de R$1000: {acima1000}')
print(f'C) Nome do produto mais barato: {barato} (R$ {min:.2f})')