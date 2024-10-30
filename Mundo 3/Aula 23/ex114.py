#Crie um codigo em python que teste se o site Pudim está acessivel pelo computador usado

import requests

def verifica_site(url):
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            print(f"O site {url} está acessível!")
        else:
            print(f"O site {url} retornou o status {resposta.status_code}.")
    except requests.exceptions.RequestException as e:
        
        print(f"O site {url} não está acessível. Erro: {e}")


url_pudim = "http://www.pudim.com.br"
verifica_site(url_pudim)
