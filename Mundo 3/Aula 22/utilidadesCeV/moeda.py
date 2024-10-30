# utilidadesCeV/moeda.py

def aumentar(preco, percentual, formatar=False):
    resultado = preco + (preco * percentual / 100)
    return moeda(resultado) if formatar else resultado

def diminuir(preco, percentual, formatar=False):
    resultado = preco - (preco * percentual / 100)
    return moeda(resultado) if formatar else resultado

def dobrar(preco, formatar=False):
    resultado = preco * 2
    return moeda(resultado) if formatar else resultado

def metade(preco, formatar=False):
    resultado = preco / 2
    return moeda(resultado) if formatar else resultado

def moeda(preco):
    return f'R$ {preco:.2f}'.replace('.', ',')

def resumo(preco, aumento, reducao, formatar=False):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco) if formatar else preco}')
    print(f'Dobro do preço: {dobrar(preco, formatar)}')
    print(f'Metade do preço: {metade(preco, formatar)}')
    print(f'Aumentando {aumento}%, temos: {aumentar(preco, aumento, formatar)}')
    print(f'Reduzindo {reducao}%, temos: {diminuir(preco, reducao, formatar)}')
    print('-' * 30)
