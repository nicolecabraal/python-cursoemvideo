#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 

#cotação do dólar hoje 11/09/2024 = R$5.64

money = float(input('Digite o valor em reais que você possui em sua carteira:'))

dolar = money*5.64

print(f'Com {money} reais, você consegue comprar {dolar} dólares')