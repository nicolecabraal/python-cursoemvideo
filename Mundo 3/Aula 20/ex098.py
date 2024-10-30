#Faça um programa que tenha uma função chamada contador(), que receba tres parametros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar tres contagens atraves da função criada:
#A) De 1 ate 10, de 1 em 1
#B) De 10 ate 0, de 2 em 2 
#C) Uma contagem personalizada

from time import sleep  

def contador(inicio, fim, passo):
    if passo == 0:  #verifica se o passo é 0 e ajusta para 1 para evitar erro
        passo = 1
    if passo < 0:  #se o passo for negativo, mantém o valor para contagem decrescente
        passo = -passo
    
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    
    if inicio < fim: 
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.3)
    else:  
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            sleep(0.3)
    
    print('FIM!')
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
