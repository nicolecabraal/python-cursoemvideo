# utilidadesCeV/dado.py

import random

def sortear_dado():
    """Simula o lançamento de um dado de 6 lados."""
    return random.randint(1, 6)

def sortear_dados(qtd):
    """Simula o lançamento de múltiplos dados de 6 lados."""
    return [sortear_dado() for _ in range(qtd)]

def media_dados(dados):
    """Calcula a média dos valores dos dados."""
    if len(dados) == 0:
        return 0
    return sum(dados) / len(dados)

def maior_dado(dados):
    """Retorna o maior valor entre os dados lançados."""
    return max(dados) if dados else None

def menor_dado(dados):
    """Retorna o menor valor entre os dados lançados."""
    return min(dados) if dados else None

def leiaDinheiro(msg):
    """Função para ler um valor monetário com validação."""
    while True:
        entrada = input(msg).replace(',', '.').strip()  # Substitui vírgula por ponto
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
