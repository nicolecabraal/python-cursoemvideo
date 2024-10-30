#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno. 

def area(a, b):
    print(f'A largura é {a} e o comprimento é {b}')
    area = a * b
    print(f' A área do terreno é de: {area}m²')

largura = float(input('Digite a largura do terreno(em metros): '))
comprimento= float(input('Digite o comprimento do terreno (em metros): '))

area(largura, comprimento)
