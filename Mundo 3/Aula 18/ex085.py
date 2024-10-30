#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = []
numpar = []
numimpar = []

for i in range (7):
    valor = int(input(f'Digite o {i+1}º valor: '))

    if valor %2 == 0:
        numpar.append(valor)
    else:
        numimpar.append(valor)

numpar.sort()
numimpar.sort()

numeros.append(numpar)
numeros.append(numimpar)

print(f'Valores pares em ordem crescente: {numeros[0]}')
print(f'Valores ímpares em ordem crescente: {numeros[1]}')
