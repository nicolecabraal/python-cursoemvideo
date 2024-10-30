#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#A vista dinheiro/cheque: 10% de desconto
#A vista no cartao: 5% de desconto
#Em ate 2x no cartao: preco normal 
#3X ou mais: 20% de juros 

preco = float(input("Digite o preço do produto: R$ "))

print("""
Escolha a condição de pagamento:
[1] À vista no dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)
""")

opcao = int(input("Digite a opção de pagamento: "))


if opcao == 1:
    valor_final = preco - (preco * 0.10)  #10% 
    print(f"O valor a ser pago à vista no dinheiro/cheque é: R$ {valor_final:.2f}")
elif opcao == 2:
    valor_final = preco - (preco * 0.05)  #5% 
    print(f"O valor a ser pago à vista no cartão é: R$ {valor_final:.2f}")
elif opcao == 3:
    valor_final = preco  #normal
    print(f"O valor a ser pago em até 2x no cartão é: R$ {valor_final:.2f} (sem juros)")
elif opcao == 4:
    valor_final = preco + (preco * 0.20)  #20% 
    print(f"O valor a ser pago em 3x ou mais no cartão é: R$ {valor_final:.2f}")
else:
    print("Opção inválida. Tente novamente.")
