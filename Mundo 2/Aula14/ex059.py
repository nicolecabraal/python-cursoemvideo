#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números 
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso

n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))

opcao = 0

while opcao !=5:
    print("\nO que você quer fazer?")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")

    opcao = int(input('Qual opção você deseja?'))

    if opcao ==1:
        resultado = n1 + n2
        print(f'A soma de {n1} e {n2} é igual a {resultado}')
    
    elif opcao == 2:
        resultado = n1 * n2
        print (f'A multiplicação entre {n1} e {n2} é igual a {resultado}')
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
    
    elif opcao == 4:
        n1 = float(input("Digite o novo primeiro valor: "))
        n2 = float(input("Digite o novo segundo valor: "))
    
    elif opcao == 5:
        print("Saindo do programa... Até mais!")
    
    else:
        print('Opção inválida. Tente novamente.')