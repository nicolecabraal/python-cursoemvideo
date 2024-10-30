#Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher so que agora utilizando um laço for.

num = int(input('Digite um npumero para ver sua tabuada:'))

print(f'\nTabuada do {num}')

for i in range (1,11):
    print(f'{num} x {i} = {num * i}')


#Esse código solicita que o usuário insira um número e, em seguida, utiliza um laço for para exibir a tabuada desse número de 1 a 10. Cada multiplicação é mostrada no formato número x i = resultado.

#A barra invertida (\) seguida da letra n (\n) é uma sequência de escape que representa uma quebra de linha (ou "nova linha") em muitas linguagens de programação, incluindo Python. Quando você usa \n em uma string, o programa entende que você quer começar uma nova linha no ponto onde essa sequência aparece. Isso é útil para formatar a saída do texto, tornando-o mais legível.