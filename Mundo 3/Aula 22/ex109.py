#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(). desenvolvida no desafio 108. 

import moeda

preco = 120

#formatado
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobrar(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(preco, 10, True)}')

print('-' * 30)

#sem formatação
print(f'O dobro de {preco} é {moeda.dobrar(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(preco, 10)}')