galera = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3): 
    dado.append(str(input('Nome:'))) #adiciona nome aos dados 
    dado.append(int(input('Idade:'))) #adiciona idade aos dados
    galera.append(dado[:]) #coloca os dados dentro da galera
    dado.clear() #limpa a lista auxiliar pra prox entrada

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
