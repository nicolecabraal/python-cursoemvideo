# utilidades/listagem.py

def listagem (arquivo):
    """
    Lista todas as pessoas cadastradas no arquivo.
    """
    try:
        with open(arquivo, 'r') as f:
            pessoas = f.readlines()
        
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return
        
        print("Pessoas cadastradas:")
        for pessoa in pessoas:
            nome, idade = pessoa.strip().split(',')
            print(f"Nome: {nome}, Idade: {idade}")
    except FileNotFoundError:
        print("Nenhum registro encontrado. Cadastre uma pessoa primeiro.")
