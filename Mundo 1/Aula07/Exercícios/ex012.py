#Faça um algoritimo que leia o preco de um produto e mostre seu novo preco com 5% de desconto. 

preco = float(input('Qual o valor do produto?'))

desconto = preco*0.05

novo_preco = preco - desconto

print (f'O preço do produto selecionado com 5% de desconto é: R${novo_preco:.2f}')