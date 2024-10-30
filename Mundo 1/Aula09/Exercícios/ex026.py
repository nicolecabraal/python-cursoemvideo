#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = input('Digite uma frase:')

a = frase.lower().count('a')
findfirst = frase.lower().find('a')
findlast = frase.lower().rfind('a')

print (f"A letra 'a' aparece {a} vezes nesta frase!")
if findfirst != -1:
    print(f"A letra 'a' aparece pela primeira vez na posição {findfirst}.")
else:
    print("A letra 'a' não aparece na frase.")
    
if findlast != -1:
    print(f"A letra 'a' aparece pela última vez na posição {findlast}.")
else:
    print("A letra 'a' não aparece na frase.")