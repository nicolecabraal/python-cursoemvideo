#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

# Leitura do primeiro termo e da razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicialização das variáveis
termo = primeiro_termo  # O primeiro termo da PA
contador = 1  # Contador para controlar os termos exibidos
total_termos = 10  # Começa mostrando 10 termos
mais_termos = 10   # Inicialmente queremos mostrar 10 termos

# Laço para mostrar os termos da PA
while mais_termos != 0:
    while contador <= total_termos:
        print(f"{termo}", end=" → ")
        termo += razao
        contador += 1
    print("Pausa")
    
    # Pergunta ao usuário se quer mostrar mais termos
    mais_termos = int(input("Quantos termos você quer mostrar a mais? (Digite 0 para encerrar): "))
    
    total_termos += mais_termos  # Atualiza o total de termos a serem exibidos

print("Progressão finalizada!")
