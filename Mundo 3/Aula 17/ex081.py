#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
#A) Quantos números foram digitados. 
#B) A lista de valores ordenada de forma decrescente. 
#C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    num = int(input('Digite um número inteiro (ou "sair" para encerrar):'))
    valores.append(num)

    continuar = input('Deseja continuar? (s/n):').strip().lower()
    if continuar == 'n':
        break

quantidade = len(valores)
print(f'Quantidade de números digitados: {quantidade}')

valores.sort(reverse=True)
print(f'A lista de valores ordenada de forma descrescente:')

if 5 in valores:
    print(f'O número 5 foi digitado e está presente na lista.')
else:
    print(f'O número 5 não foi digitado.')