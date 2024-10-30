#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso. 

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20:'))

    if 0 <= numero <= 20:
        print(f'Você digitou o número {extenso[numero]}')
        break
    else:
        print('Número inválido. Tente novamente')

#A tupla 'extenso' armazena os números por extenso, e cada item da tupla tem uma posição, chamada de índice. Em Python, as listas e tuplas são indexadas começando pelo número 0.

