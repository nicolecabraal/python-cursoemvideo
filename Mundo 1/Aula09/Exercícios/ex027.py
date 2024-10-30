#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. 
#Exemplo: Ana Maria de Souza 
#primeiro: Ana 
#ultimo: Souza


nome = input("Digite seu nome completo: ")

n = nome.strip().split()

primeiro_nome = n[0]
ultimo_nome = n[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
