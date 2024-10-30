#Crie um pgrograma que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# Inicialização das variáveis
soma = 0
contador = 0
maior = None
menor = None

while True:
    # Lê um número inteiro
    numero = int(input("Digite um número inteiro: "))
    
    # Atualiza soma e contador
    soma += numero
    contador += 1
    
    # Verifica maior e menor número
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    
    # Pergunta se o usuário quer continuar
    continuar = input("Você quer continuar a digitar valores? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Cálculo da média
if contador > 0:
    media = soma / contador
    print(f"A média dos valores digitados é: {media}")
    print(f"O maior valor lido foi: {maior}")
    print(f"O menor valor lido foi: {menor}")
else:
    print("Nenhum valor foi digitado.")
