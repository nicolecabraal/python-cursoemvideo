#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:

#A) Quantas pessoas tem mais de 18 anos.
#B)Quantos homens foram cadastrados
#C)Quantas mulheres tem menos de 20 anos.

maioridade = 0
homens = 0
mulheresmenos20 = 0

while True:
    idade = int(input('Digite sua idade:'))
    sexo = input('Digite seu sexo [F/M]:').strip().upper()

    if idade > 18:
        maioridade += 1

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    continuar = input('Deseja continuar? [S/N]:').strip().upper()
    if continuar != 'S':
        break

print(f'A) Pessoas com mais de 18 anos: {maioridade}')
print(f'B) Homens cadastrados: {homens}')
print(f'C) Mulheres com menos de 20 anos: {mulheresmenos20}')
