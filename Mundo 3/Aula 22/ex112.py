#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um m´dulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários. 

from utilidadesCeV import dado


valor = dado.leiaDinheiro('Digite um valor monetário: ')
print(f'O valor inserido foi: R$ {valor:.2f}')
