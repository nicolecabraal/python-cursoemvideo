#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobrar() e metade(). Faça também um programa que importe esse modulo e use algumas dessas funções. 

import moeda

preco = 145

print(f'O dobro de {preco} é {moeda.dobrar(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(preco, 10)}')