#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))


if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As retas podem formar um triângulo.")
else:
    print("As retas NÃO podem formar um triângulo.")

#Para que três retas formem um triângulo, é necessário que a soma de quaisquer dois lados seja maior que o terceiro. O programa verifica essa condição para todas as combinações de lados. Se todas forem verdadeiras, as retas podem formar um triângulo; caso contrário, não podem.