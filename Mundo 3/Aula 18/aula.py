#aprendendo a colocar uma lista dentro da outra 

teste = list()
teste.append('Nicole')
teste.append(23)

galera = list()
galera.append(teste[:]) #lembrar de botar o colchete com 2 pontos pq vai criar uma COPIA
teste [0] = 'Maria'
teste [1] = 22
galera.append(teste[:])

print(galera)

