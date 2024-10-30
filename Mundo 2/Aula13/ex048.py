#Faça um programa que calcule a soma entre todos os números impares que são multriplos de três e que se encontram no intervalo de 1 a 500

soma = 0

for num in range(1,501):
    if num % 2 != 0 and num % 3 == 0:
        soma += num
    
print(f'A soma de todos os numeros impares entre 1 e 500 é igual a {soma}')