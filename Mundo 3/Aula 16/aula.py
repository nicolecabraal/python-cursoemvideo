lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])
print(lanche[1:3])
print(lanche[-1])
print(lanche[:2])

#tambem funciona sem os parenteses, é uma atualização do python.

#tuplas sao IMUTAVEIS


for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Eu comi pra caramba.')


for cont in range (0, len(lanche)):
    print(cont)


for cont in range (0, len(lanche)):
    print(lanche[cont])


#Podemos criar três tuplas e colocar uma como soma 
a = (2, 5, 4)
b = (5, 8 , 1 , 2)
c = a + b
#Neste caso, não vai rolar uma soma e sim juntar as duas duplas, ficando como resultado  --> (2, 5, 4, 5, 8 , 1 , 2 )

