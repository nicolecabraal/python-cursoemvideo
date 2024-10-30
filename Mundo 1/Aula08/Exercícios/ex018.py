#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math

angulo = float(input('Digite um ângulo em graus:'))

rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'Seno de {angulo}°: {seno:.4f}')
print(f'Cosseno de {angulo}°: {cosseno:.4f}')
print(f'Tangente de {angulo}°: {tangente:.4f}')

#A função math.radians converde o angulo para radianos, ja que as funções trigonometricas do python (sin, cos, tan) operam em radianos