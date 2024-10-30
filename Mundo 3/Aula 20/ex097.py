#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel 
#ex : escreva ('ola mundo') saida : tem aquelas linhas print('--' *30)

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}  ')
    print('-' * tam)

escreva('Olá, mundo!')
escreva('Python é incrível!')
escreva('Curso de Programação do Curso em Video')