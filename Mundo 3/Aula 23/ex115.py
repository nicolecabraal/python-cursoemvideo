#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema so vai ter duas opcoes: cadastras uma nova pessoa e listar todas as pessoas cadastradas

from utilidades.cadastro import cadastro
from utilidades.listagem import listagem
from utilidades import linha, cabecalho, menu  

def main():
    """
    Função principal do sistema.

    """
    arquivo = "pessoas.txt"
    
    while True:
        opcoes = ['Cadastrar nova pessoa', 'Listar pessoas cadastradas', 'Sair']
        menu(opcoes)  
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastro(arquivo)
        elif opcao == '2':
            listagem(arquivo)
        elif opcao == '3':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
