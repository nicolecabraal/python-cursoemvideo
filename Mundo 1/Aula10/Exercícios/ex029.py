#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite. 

velocidade = float(input('Digite a velocidade do carro em Km/h'))

if velocidade > 80:
    print('MULTADO')
    multa = (velocidade-80) *7
    print(f'Você ultrapassou a velocidade e foi multado.')
    print(f'O valor da multa é de R${multa:.2f}')
else:
    print('Você está dentro do limite de velocidade')