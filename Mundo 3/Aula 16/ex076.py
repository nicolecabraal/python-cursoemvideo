#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia. No final, mostre uma listagem de preços organizando os dados em forma tabular. 

produtos = (
    'Lápis', 1.50,
    'Caderno', 10.90,
    'Borracha', 2.00,
    'Caneta', 3.50,
    'Mochila', 120.00,
    'Livro', 45.90,
    'Estojo', 15.00,
    'Régua', 3.80
)

print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)

for i in range(0, len(produtos), 2):
    produto = produtos[i]
    preco = produtos[i+1]
    print(f'{produto:<30} R$ {preco:>7.2f}')

print("-" * 40)