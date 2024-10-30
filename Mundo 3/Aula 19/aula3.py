estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #é tipo o [:] só que em dicionarios nao pode fazer fatiamento, tem o método copy(), que intuitivamente: FAZ UMA COPIA

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')