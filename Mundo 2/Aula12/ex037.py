#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input('Digite um número inteiro:'))

print('''Escolha uma das bases para conversão:
    [1] Para converter para BINÁRIO
    [2] Para converter para OCTAL 
    [3] Para converter para HEXADECIMAL''')

opcao = int(input('Sua opção:'))

if opcao == 1:
    print(f"{numero} convertido para Binário é {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido para Octal é {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} convertido para Hexadecimal é {hex(numero)[2:].upper()}")
else:
    print("Opção inválida. Tente novamente.")