#Tornar menos repetitivo, criar uma "rotina"

def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)


print('--' *30)
#Outra maneira de fazer:

def soma (a, b):
    print(f'A = {a} e B={b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)