#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo:')
print('O tipo primitivo deste valor é', type(a))

print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalphanum())
print('Está em maiusculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())

#a letra 'a' é o objeto, todos os objetos tem características e realizam funcionaliadades. Eles tem atributos e métodos. Neste caso é metodos devido aos parenteses depois. 