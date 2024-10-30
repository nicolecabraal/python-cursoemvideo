#Escreva um programa que leia um número n inteiro qualuqer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

# Função para calcular a sequência de Fibonacci
def fibonacci(n):
    fib_sequence = []  # Lista para armazenar a sequência
    a, b = 0, 1  # Inicializa os dois primeiros termos

    for _ in range(n):
        fib_sequence.append(a)  # Adiciona o termo atual à lista
        a, b = b, a + b  # Atualiza a e b para os próximos termos

    return fib_sequence

# Leitura do número inteiro n
n = int(input("Digite um número inteiro: "))

# Exibindo os n primeiros elementos da sequência de Fibonacci
print(f"Os primeiros {n} elementos da sequência de Fibonacci são: {fibonacci(n)}")
