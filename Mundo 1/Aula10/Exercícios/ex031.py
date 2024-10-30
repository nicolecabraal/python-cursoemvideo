#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de ate 200km e R$0,45 para viagens mais longas. 

distancia = float(input('Digite a distância da viagem em Km/h:'))

if distancia <= 200:
    passagem1 = distancia * 0.50
    print(f'O valor da passagem é de: {passagem1}')
else:
    passagem2 = distancia *0.45
    print(f'O valor da passagem é de: {passagem2}')
