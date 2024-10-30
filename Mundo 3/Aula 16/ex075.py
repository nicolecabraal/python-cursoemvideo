#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#Quantas vezes apareceu o valor 9. 
#Em que posição foi digitado o primeiro valor 3. 
#Quais foram os números pares

valores = tuple(int(input(f'Digite o {i+1} valor:)')) for i in range(4))

quantidade_nove = valores.count(9)
print(f'O valor 9 apareceu {quantidade_nove} vezes.')

if 3 in valores:
    posicao_tres = valores. index(2) +1
    print(f'O valor 3 apareceu na {posicao_tres} posição')
else:
    print('O valor 3 não foi digitado.')

pares = tuple(num for num in valores if num % 2== 0)
print(f'Os números pares digitados foram: {pares if pares else 'Nenhum numero par foi digitado.'}')