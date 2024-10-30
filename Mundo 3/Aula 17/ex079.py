#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente. 

valores = []

while True:
    valor = float(input("Digite um valor (ou 'sair' para encerrar):"))

    if valor not in valores:
        valores.append(valor)
        print(f'Valor {valor} adicionado com sucesso.')
    else:
        print(f'O valor {valor} já existe na lista. Não vou adicioná-lo.')
    
    continuar = input('Deseja continuar? (s/n):').strip().lower()
    if continuar == 'n':
        break

valores.sort()
print(f'Valores únicos digitados: {valores}')