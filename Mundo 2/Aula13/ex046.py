#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 à 0, com uma pausa de 1 segundo entre eles

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)


print('BOOOOOOOOOOOOOOOOOOOM!!!!!!')

#O código usa um loop *for* que começa em 10 e vai até 0 (o -1 é o passo que indica que a contagem é decrescente), e a função time.sleep(1) faz o programa pausar por 1 segundo entre cada número. Quando a contagem chega a 0, ele exibe a mensagem de estouro. 
