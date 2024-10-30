#Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário. O programa será interrompido quando o numero solicitado for negativo.

while True:
    n = int(input('Digite um número para ver a tabuada (num negativo para parar):'))
    if n < 0:
        break
    print(f'Tabuada do {n}')
    for i in range(1,11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 20)