valores = list()
valores.append(5)
valores.append(2)
valores.append(8)
valores.append(6)
valores.append(9)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


# tambem pode ser feito com input 

valores = list ()
for cont in range (0,5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
