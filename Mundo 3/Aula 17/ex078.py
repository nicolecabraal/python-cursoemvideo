#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

valores = [] #vai fazer a lista

for i in range(5):
    valor = float(input(f'Digite o {i+1}º valor:'))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

pmaior = valores.index(maior)
pmenor = valores.index(menor)

print(f'O maior valor digitado foi: {maior} na posição {pmaior}')
print(f'O menor valor digitado foi: {menor} na posição {pmenor}')