#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flog)

# Inicialização das variáveis
soma = 0
contador = 0

# Laço para ler os números
while True:
    numero = int(input("Digite um número inteiro (ou 999 para parar): "))
    
    # Condição de parada
    if numero == 999:
        break
    
    # Atualiza a soma e o contador
    soma += numero
    contador += 1

# Exibe os resultados
print(f"Você digitou {contador} números.")
print(f"A soma entre eles é: {soma}.")
