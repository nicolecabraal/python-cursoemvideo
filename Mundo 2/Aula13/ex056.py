#Desenvolva um programa que leia: nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos

# Inicializa variáveis
soma_idade = 0
maior_idade = 0
nome_homem_mais_velho = ""
contador_mulheres_menores_20 = 0

# Loop para ler as informações de 4 pessoas
for i in range(4):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i + 1}ª pessoa (M/F): ").strip().upper()
    
    # Soma a idade para calcular a média
    soma_idade += idade
    
    # Verifica se é homem e se ele é o mais velho
    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_homem_mais_velho = nome
    
    # Verifica se é mulher e se tem menos de 20 anos
    elif sexo == 'F' and idade < 20:
        contador_mulheres_menores_20 += 1

# Cálculo da média de idade
media_idade = soma_idade / 4

# Exibe os resultados
print(f"\nA média de idade do grupo é: {media_idade:.2f} anos")
print(f"O homem mais velho é: {nome_homem_mais_velho} com {maior_idade} anos")
print(f"Número de mulheres com menos de 20 anos: {contador_mulheres_menores_20}")
