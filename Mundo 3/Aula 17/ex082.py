#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente. Ao final, mostre o conteudo das tres listas geradas. 

valores = []
par = []
impar = []

while True:
    num =  int(input('Digite um número inteiro (ou "sair" parra encerrar):'))

    valores.append(num)

    if num %2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    continuar = input('Deseja continuar? (s/n):').strip().lower()
    if continuar == 'n':
        break

print(f'Você digitou esses valores {valores}')
print(f'Lista com os valores pares: {par}')
print(f'Lista com os valores ímpares: {impar}')