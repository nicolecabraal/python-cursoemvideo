#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
#Apenas os 5 primeiros colocados 
#Os ultimos 4 colocados da tabela 
#Uma lista com os times em ordem alfabetica
#Em que posição na tabela está o time da chapecoense

times_brasileirao = (
    'Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 
    'Athletico-PR', 'São Paulo', 'Cruzeiro', 'Internacional', 'Fortaleza', 
    'Bragantino', 'Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá', 
    'Bahia', 'Vasco', 'Coritiba', 'América-MG', 'Chapecoense'
)

times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atletico-MG', 'Gremio', 'Criciuma', 'Bragantino', 'Juventude', 'Atletico Paranaense', 'Fluminense', 'EC Vitória', 'Corinthians', 'Cuiabá', 'Atlético-GO')

print('Os cinco primeiros colocados são:')
print(times[:5])

print('\nOs 4 últimos colocados são:')
print(times[-4])

print('\nTimes em ordem alfabética:')
print(sorted(times))

if 'Chapecoense' in times:
    chapecoense_posi = times.index('Chapecoense') +1 #Pega o índice e soma 1 (pois índice começa do 0)
    print (f'\nA chapecoense está na {chapecoense_posi} posição')
else:
    print('\n A Chapecoense foi rebaixada.')