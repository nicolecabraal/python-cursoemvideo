#Faça um programa que tenha uma função chamada maior(), que receba varios parametros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior.
def maior(*numeros):
    if len(numeros) == 0:
        print("Nenhum número foi informado.")
    else:
        maior_numero = max(numeros)  
        print(f'Analisando os valores {numeros}...')
        print(f'O maior valor informado foi {maior_numero}.')
        print('-' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(10, 15, 3)
maior(8)
maior()
