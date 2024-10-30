#Crie um programa que tenha a funcao leiaInt(), que vai funcionar de forma semelhante à funcao input() do python, so que fazendo a validação para aceitar apenas um valor numerico. Ex: n=leiaInt('Digite um n')

def leiaInt(msg):
    """
    Função que solicita ao usuário um valor inteiro, validando a entrada.

    :param msg: Mensagem que será exibida ao solicitar o número
    :return: Um valor inteiro validado
    """


    while True:
        valor = input(msg)
        
        if valor.isdigit():
            return int(valor)  
        else:
            print("Erro! Digite um número inteiro válido.")


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")