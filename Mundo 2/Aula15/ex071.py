#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues. 

#OBS: Considere que o caixa possui cedulas de 50, 20, 10 e 1 

#vamos iniciar o programa com as cedulas disponiveis:

cedulas = [50, 20, 10, 1]

saque = int(input('Digite o valor a ser sacado:'))

quantidade_cedulas = {} #aqui criamos um dicionario pra armazenar a quantidade de cédulas

if saque <= 0:
    print('Valor inválido. O valor inserido deve ser um número inteiro positivo. Tente novamente')
else:
    for cedula in cedulas:
        quantidade =  saque // cedula #calcula a quantidade de cedulas daquele valor sao necessarias

        if quantidade > 0:
            quantidade_cedulas[cedula] = quantidade
        
        saque -= quantidade * cedula

    print('Cédulas a serem entregues:')
    for cedula, quantidade in quantidade_cedulas.items():
        print(f'R${cedula}: {quantidade} cédula(s)')