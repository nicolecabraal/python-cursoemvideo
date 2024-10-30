#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flog)

s = 0 #soma
cont = 0 #contador
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n #soma dos numeros. "Pega o valor atual de SS e adiciona o valor de n nele"
    cont += 1 #conta quandos num foram digitados, ou seja, quantas vezes o laço rodou.
print(f' Você digitou {cont} números e a soma vale {s}')
