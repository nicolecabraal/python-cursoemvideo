#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços. 

frase = str(input('Digite uma frase:'))

nospace = frase.replace(" ", " ").lower()

if nospace == nospace [::-1]:
    print('A frase é um palindromo')
else:
    print('A frase não é um palíndromo.')


#frase.replace(" ", ""): Remove todos os espaços da frase.
#.lower(): Converte todos os caracteres da frase para minúsculas para garantir que a comparação não seja afetada por diferenças de maiúsculas e minúsculas

#Verificação de Palíndromo:
#nospace[::-1]: Inverte a string para verificar se ela é igual à original.
#A condição compara a frase sem espaços e a versão invertida dela. Se forem iguais, a frase é um palíndromo