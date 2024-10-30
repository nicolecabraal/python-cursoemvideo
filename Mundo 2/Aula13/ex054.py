#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores. 

# Importa a biblioteca datetime para obter o ano atual
from datetime import datetime

# Obtém o ano atual
ano_atual = datetime.now().year

# Inicializa contadores
maiores = 0
menores = 0

# Loop para ler o ano de nascimento de 7 pessoas
for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    idade = ano_atual - ano_nascimento  # Calcula a idade

    # Verifica se a pessoa é maior ou menor de idade
    if idade < 18:
        menores += 1
    else:
        maiores += 1

# Exibe o resultado
print(f"\nTotal de pessoas menores de idade: {menores}")
print(f"Total de pessoas maiores de idade: {maiores}")
