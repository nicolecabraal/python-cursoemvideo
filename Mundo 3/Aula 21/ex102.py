#Crie um programa que tenha uma funcao fatorial que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show que sera um valor logico (opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial. 

def fatorial(num, show=False): #quando você define show=False na assinatura da função, está dizendo que, se o usuário não passar um valor para o parâmetro show ao chamar a função, ele será automaticamente considerado como False.

    """
    Calcula o fatorial de um número.

    :param num: O número para calcular o fatorial
    :param show: (Opcional) Mostra ou não o processo de cálculo do fatorial
    :return: O valor do fatorial de num
    """

    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i > 1:
                print(f"{i} x ", end="")
            else:
                print(f"{i} = ", end="")
    return f


n = int(input("Digite um número para calcular o fatorial: "))
mostrar = input("Deseja ver o processo de cálculo? (S/N): ").strip().upper() == 'S'


resultado = fatorial(n, mostrar)
print(f"O fatorial de {n} é {resultado}")

