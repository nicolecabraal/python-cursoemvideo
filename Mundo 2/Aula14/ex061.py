#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostraNDO OS 10 primeiros termos da progressão usando a aestrutura while


primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))


termo = primeiro_termo  # O primeiro termo da PA
contador = 1  # Contador para controlar os 10 termos

while contador <= 10:
    print(f"{termo}", end=" → ")
    termo += razao  # Calcula o próximo termo somando a razão
    contador += 1   # Incrementa o contador

print("Fim!")
