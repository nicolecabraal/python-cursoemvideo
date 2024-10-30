#Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal 
#25 ate 30: Sobrepeso
#30 a 40: Obesidade
#Acima de 40: Obesidade morbida

peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura ** 2)


print(f"Seu IMC é {imc:.1f}")

if imc < 18.5:
    print("Status: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Status: Peso ideal")
elif 25 <= imc < 30:
    print("Status: Sobrepeso")
elif 30 <= imc <= 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")
