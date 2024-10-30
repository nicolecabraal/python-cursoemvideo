#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 
#Adicionei por conta própria um sistema de aprovado/reprovado. 

def calcular_media(notas):
    return sum(notas) / len(notas)

def exibir_boletim(alunos):
    print('-=' * 30)
    print('Boletim: ')

    for aluno in alunos:
        nome, notas = aluno [0], aluno [1:]
        media = calcular_media(notas)
        status = 'Aprovado' if media >= 7 else 'Reprovado'
        print(f'Aluno: {nome}, Média: {media:.2f}, Status: {status}.')

def mostrarnotasindividuais (alunos):
    while True:
        nome = input('Digite o nome do aluno para ver as notas (ou "sair" para encerrar): ')
        if nome.lower() == 'sair':
            break
        else:
            print('Aluno não encontrado.')

def main():
    alunos = []
    while True:
        nome = input('Nome do aluno:')
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        alunos.append([nome, nota1, nota2])

        continuar = input('Deseja adicionar outro aluno? (s/n): ').strip().lower()
        if continuar != 's':
            break

    exibir_boletim(alunos)
    mostrarnotasindividuais(alunos)


if __name__ == '__main__':
    main()