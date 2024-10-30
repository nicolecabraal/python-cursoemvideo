def cadastro (arquivo):
    """
    Cadastra uma nova pessoa no arquivo 

    """
    nome = input('Digite o nome da pessoa:')
    idade = input('Digite a idade da pessoa:')

    with open (arquivo, 'a') as f:
        f.write(f'{nome}, {idade}\n')
    
    print(f'Pessoa {nome} cadastrada com sucesso!')