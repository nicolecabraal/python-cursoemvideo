#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite o valor em metros:'))

centimetro = metro*100
milimetro = metro*1000

print (f'{metro} em centímetros = {centimetro} \n {metro} em milímetros = {milimetro}')