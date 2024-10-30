#Faça um programa que leia três números e mostre qual o maior e qual o menor. 

n1 = float(input('Digiteo primeiro número:'))
n2 = float(input('Digiteo segundo número:'))
n3 = float(input('Digiteo terceiro número:'))

menor = min(n1,n2,n3)
maior = max(n1,n2,n3)

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')