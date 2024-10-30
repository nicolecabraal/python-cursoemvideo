#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t1 = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))

print('Os dez primeiros termos da PA são:')
for i in range(10):
    atual = t1 + i * razao
    print(atual)