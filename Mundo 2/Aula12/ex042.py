#Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado. 
#Equilatero: todos os lados sao iguais 
#Isosceles: dois lados iguais 
#Escaleno: todos os lados diferentes

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os segmentos podem formar um triângulo!", end=" ")

    if lado1 == lado2 == lado3:
        print("Tipo de triângulo: EQUILÁTERO (todos os lados iguais)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo de triângulo: ISÓSCELES (dois lados iguais)")
    else:
        print("Tipo de triângulo: ESCALENO (todos os lados diferentes)")
else:
    print("Os segmentos NÃO podem formar um triângulo.")
