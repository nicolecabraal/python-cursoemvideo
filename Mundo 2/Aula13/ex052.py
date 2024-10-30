#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

def primo(num):
    if num <= 1:
        return False #numeros menores ou iguais a 1 nao sao primos
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False #se for divisivel por algum numero entre 2 e a raiz quadrada de num, não é primo
        return True # se nao for divisivel por nenhum desses, é primo.
    

num = int(input('Digite um número inteiro:'))

if primo(num):
    print(f'{num} é primo')
else:
    print(f'{num} NÃO é primo')


#Explicação:
#Função primo:

#A função recebe um número e verifica se ele é primo.
#Se o número for menor ou igual a 1, retorna False (números menores ou iguais a 1 não são primos).
#Um laço for percorre os números de 2 até a raiz quadrada do número. Isso é eficiente, pois não é necessário verificar divisores além da raiz quadrada.
#Se o número for divisível por qualquer um desses números (numero % i == 0), retorna False.
#Se não for divisível por nenhum, retorna True, indicando que o número é primo.
#Entrada do Usuário:

#O programa solicita ao usuário que insira um número inteiro.
#Verificação e Saída:

#O programa chama a função primo para verificar se o número é primo e imprime o resultado.