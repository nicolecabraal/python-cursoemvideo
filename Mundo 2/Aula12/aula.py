nome = str(input('Qual seu nome?'))

if nome == 'Nicole':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {nome}!')

#A estrutura deve começar sempre com if, posso ter quantos elif quiser e apenas um else. O else nem sempre é necessário. 