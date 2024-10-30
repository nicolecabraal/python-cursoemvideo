#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando. 

from utilidadesCeV import moeda, dado


preco = 100  
aumento = 10  
reducao = 15  

print("=== Resumo do Preço ===")
moeda.resumo(preco, aumento, reducao, True)


qtd_dados = 3
resultados = dado.sortear_dados(qtd_dados)

print(f"\n=== Resultados dos Lançamentos de Dados ===")
print(f"Lançados: {resultados}")
print(f"Média: {dado.media_dados(resultados):.2f}")
print(f"Maior valor: {dado.maior_dado(resultados)}")
print(f"Menor valor: {dado.menor_dado(resultados)}")
