#Faça um programa que leia um numero e mostre o seu fatorial
#Exemplo: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um número inteiro:'))

fatorial = 1
contador = num

print(f'Calculando {num} = ', end="") #O parâmetro end="" na função print() é usado para definir o que será colocado no final da linha após a impressão. Por padrão, o print() sempre termina com uma nova linha (\n). No entanto, você pode alterar esse comportamento. Nesse caso, estou pedindo para que o python nao pule para a proxima linha depois de imprimir o calculando {num} =. Isso significa que o que vier impresso depois, vai aparecer na mesma linha.

while contador > 0:
    print(f'{contador}', end="")
    if contador > 1:
        print(' x ', end="")
    else:
        print(' = ', end="")
    

    fatorial*=contador  # =  fatorial = fatorial * contador
    contador -= 1       # = contador = contador - 1

print(f'{fatorial}')
