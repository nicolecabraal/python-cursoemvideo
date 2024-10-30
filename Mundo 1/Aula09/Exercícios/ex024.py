#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = input('Digite o nome da sua cidade:')

santo = cidade.strip().startswith('Santo')

if santo :
    print("A cidade começa com 'Santo'")
else :
    print("A cidade não começa com 'Santo'")
