#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m cubicos.

largura = float(input('Digite a largura da sua parede em metros:'))
altura = float(input('Digite a altura da sua parede em metros:'))

area = largura * altura

tinta = area /2

print(f'A parede possui uma área de {area} m^2')
print(f'Você precisará de {tinta:.2f} litros de tinta para pintá-la.')

#o formato .2f exibe o resultado em duas casas decimais. 