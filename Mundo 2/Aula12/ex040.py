#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
#Média abaixo de 5: REPROVADO
#Media entre 5 e 6.9: RECUPERAÇÃO
#Media 7 ou superior: APROVADO

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1+n2) / 2

if media < 5:
    print(f'Sua média foi: {media:1f}. Você está REPROVADO')
elif 5 <= media < 6.9:
    print(f'Sua média foi: {media:1f}. Você está de RECUPERAÇÃO')
else:
    print(f'Sua média foi: {media:1f}. Parabéns! Você foi APROVADO')