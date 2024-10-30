# utilidades/__init__.py

def linha(tam=42):
    """Retorna uma linha de caracteres '-' com o tamanho especificado."""
    return '-' * tam

def cabecalho(txt):
    """Exibe um cabeçalho centralizado."""
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    """Exibe o menu principal."""
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c += 1
    print(linha())
