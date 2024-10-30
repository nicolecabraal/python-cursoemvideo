#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta. 

def verificar_parenteses(expressao):
    contador = 0

    for char in expressao:
        if char == '(':
            contador += 1
        elif char == ')':
            contador -= 1
        
        if contador < 0:
            return False
    return contador == 0

expressao = input('Digite uma expressão com parênteses:')

if verificar_parenteses(expressao):
    print('A expressão está correta!')
else:
    print('A expressão está incorreta.')