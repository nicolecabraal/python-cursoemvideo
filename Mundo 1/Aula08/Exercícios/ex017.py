#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa. 

import math
a = float(input('Digite o valor do cateto oposto:'))
b = float(input('Digite o valor do cateto adjacente:'))

hip = math.sqrt(a**2 + b**2)

print(f'O valor da hipotenusa é igual à: {hip}')