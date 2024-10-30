num = [2, 5, 9, 1] #colchetes pois é uma lista, se fosse uma tupla seriam parenteses
num[2] = 3 #transforma o terceiro elemento (pois o python começa a contagem do zero, no número 3)
num.append(7) #adiciona o número 7 no final da lista
num.sort() #vai organizar os números em ordem (se quiser em ordem decrescente, so colocar o reverse=True)
num.insert(2, 0 ) #na posição 2 coloca o numero 0 
num.pop(2) #elimina o elemento 2
print(num)
print(f'Essa lista tem {len(num)} elementos.')