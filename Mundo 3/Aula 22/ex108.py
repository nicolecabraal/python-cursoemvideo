#Adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado. 

import moeda

preco = 290  

print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobrar(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Reduzindo 10%, temos {moeda.moeda(moeda.diminuir(preco, 10))}')