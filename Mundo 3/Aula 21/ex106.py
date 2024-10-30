#Faça um mini-sistema que utilize o interactive help do python. o usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra fim o programa se encerrara. 
#obs use cores

def ajuda(comando):
    """
    Exibe o help de um comando do Python com formatação colorida.

    :param comando: Comando para o qual se deseja exibir o help.
    """
    titulo(f"Acessando o manual do comando '{comando}'", 34)
    print('\033[7;30m', end='')  #inverte as cores (fundo branco e texto preto)
    help(comando)
    print('\033[m', end='')  #reseta a cor para o padrão


def titulo(msg, cor=33):
    """
    Exibe um título formatado com uma cor.

    :param msg: Mensagem do título.
    :param cor: Código de cor ANSI (opcional).
    """
    tamanho = len(msg) + 4
    print(f'\033[{cor}m', end='')  #define a cor
    print('~' * tamanho)
    print(f"  {msg}")
    print('~' * tamanho)
    print('\033[m', end='')  #reseta a cor para o padrão


while True:
    titulo("SISTEMA DE AJUDA PYTHON", 32)
    comando = input("Função ou Biblioteca > ").strip()
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)

titulo("ATÉ LOGO!", 31)
