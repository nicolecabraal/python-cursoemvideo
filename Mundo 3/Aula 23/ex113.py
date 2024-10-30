#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero de tipo invalido. Aproveite e crie tambem uma funcao leiaFloat() com a mesma funcionalidade. 

def leiaInt(msg):
    while True:
        try:
            valor = input(msg).strip() 
            return int(valor)
        except ValueError:
            print("Erro! Digite um número inteiro válido.")

def leiaFloat(msg):
    while True:
        try:
            valor = input(msg).strip()  
            valor = valor.replace(',', '.')  
            return float(valor)
        except ValueError:
            print("Erro! Digite um número real válido.")

n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número inteiro {n}.")

f = leiaFloat("Digite um número real: ")
print(f"Você acabou de digitar o número real {f}.")
