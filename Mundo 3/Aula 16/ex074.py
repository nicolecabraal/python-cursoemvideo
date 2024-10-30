#Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. 

import random

num = tuple(random.randint(1, 100) for _ in range(5))

print('Números gerados:', num)

print(f"O maior número é: {max(num)}")
print(f"O menor número é: {min(num)}")

#random.randint(1, 100): Gera números aleatórios entre 1 e 100.
#Compreensão de lista e tupla: A expressão (random.randint(1, 100) for _ in range(5)) cria 5 números aleatórios e os coloca diretamente em uma tupla.