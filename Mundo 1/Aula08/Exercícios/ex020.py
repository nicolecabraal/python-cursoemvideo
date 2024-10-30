#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

import random

aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print(f'A ordem de apresentação será:')
for i, aluno in enumerate(alunos, start = 1):
    print(f'{i}º: {aluno}')

#O loop for exibe a ordem sorteada de apreentação com a posição numerada
#A função enumerate serve para gerar uma contagem junto com os itens da lista
#Start = 1 por padrao, enumerate começa a contagem do zero. Ao usar start=1, pedimos para contagem começar no numero 1 
#i vai receber a posição do aluno