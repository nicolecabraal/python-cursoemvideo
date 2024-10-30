#Crie um programa que tenha uma tupla com várias palavras (nao usar acentos). Depois disso, voce deve mostrar para cada palavra quais sao suas vogais. 

palavras = ('banana', 'controle', 'videogame', 'livro', 'rpg', 'mesa', 'pobre', 'cartas', 'laranja', 'van', 'pato', 'melancia', 'garrafa', 'girafa')

def extrair_vogais(palavra):
    vogais = 'aeiou'
    return [letra for letra in palavra if letra in vogais]

for palavra in palavras:
    vogais_encontradas = extrair_vogais(palavra)

    print(f"As vogais em '{palavra}' são: {', ' .join(vogais_encontradas)}")
