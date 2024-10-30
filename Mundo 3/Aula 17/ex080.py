#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-s em uma lista já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. 

valores = []
for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor:'))

    if len(valores) == 0 or valor > valores[-1]:   #aqui diz que se a lista estiver vazia, ou se o valor for maior que o ultimo elemento, o valor é adicionado no final da lista, fazendo assim, com que a lista fique ordenada.
        valores.append(valor)
    else:
        for j in range(len(valores)): #aqui o loop for serve pra encontrar a posição correta para inserir o valor, de forma que a lista  permaneça ordenada
            if valor <= valores[j]:
                valores.insert(j, valor)
                break

print(f'Lista ordenada: {valores}')