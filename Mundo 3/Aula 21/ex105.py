#Faça um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informações: 
#-Quantidade de notas 
#-A maior nota 
#-A menor nota 
#-A media da turma 
#-A situação

#Adicione tambem as docstrings da funçao

def notas(*n, situacao=False):
    """
    Função para analisar notas e situações de vários alunos.

    :param n: Recebe várias notas (números).
    :param situacao: (opcional) Indica se deve ou não adicionar a situação da turma.
    :return: Retorna um dicionário com a quantidade de notas, maior nota, menor nota, média da turma e, opcionalmente, a situação da turma.
    """

    resultado = {}
    resultado['total'] = len(n)
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    resultado['media'] = sum(n) / len(n)

    if situacao:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'BOA'
        elif 5 <= resultado['media'] < 7:
            resultado['situacao'] = 'RAZOÁVEL'
        else:
            resultado ['situacao'] = 'RUIM'
    
    return resultado


resp = notas(5.5, 7.0, 8.5, 10, 9.9, 2.5, 4.5, situacao=True)
print(resp)