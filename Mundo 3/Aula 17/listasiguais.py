a = [2, 3, 4, 7]
b = a
b[2] = 2 #o python vai alterar em ambas as listas!!!!
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#podemos mandar b receber todos os itens de A
a = [2, 3, 4, 7]
b = a[:] #cria uma CÓPIA e não uma ligação como no exemplo anterior
b[2] = 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')