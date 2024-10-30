#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido. 

# Inicializa as variáveis para armazenar o maior e menor peso
maior_peso = float('-inf')  # Começa com o menor valor possível
menor_peso = float('inf')   # Começa com o maior valor possível

# Loop para ler o peso de 5 pessoas
for i in range(5):
    peso = float(input(f"Digite o peso da {i + 1}ª pessoa (em kg): "))
    
    # Atualiza o maior peso se o peso atual for maior
    if peso > maior_peso:
        maior_peso = peso
    
    # Atualiza o menor peso se o peso atual for menor
    if peso < menor_peso:
        menor_peso = peso

# Exibe os resultados
print(f"\nO maior peso lido foi: {maior_peso} kg")
print(f"O menor peso lido foi: {menor_peso} kg")
