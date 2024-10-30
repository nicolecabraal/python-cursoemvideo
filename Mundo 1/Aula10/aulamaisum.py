n1 = float(input('Digite a primeira nota:'))
n2= float(input('Digite a segunda nota:'))
m = (n1+n2)/2

print(f'A sua média foi {m}')

if m >=6:
    print('Você passou, PARABÉNS!')
else:
    print('Sua média foi ruim. Estude mais. REPROVADO')