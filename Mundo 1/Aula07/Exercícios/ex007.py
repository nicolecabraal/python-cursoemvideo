#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite aqui a primeira nota:'))
nota2 = float(input('Digite aqui a segunda nota:'))

media = (nota1 + nota2) /2

print(f'A média entre {nota1} e {nota2} = {media}')

#resolvi adicionar uma dinâmica de aprovado/ reprovado. vamos fazer com if e else 

if media >=6:
    print('Aprovado! Parabéns')
else:
    print('Reprovado.')