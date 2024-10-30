#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Exemplo: 
#Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1


num = input('Digite um número de 0 a 9999:')

num = num.zfill(4) #preenche com zero a esqueda, caso tenha menos de 4 digitos o numero digitado

unidade = num[3]
dezena = num[2] 
centena = num[1]
milhar = num[0]

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')