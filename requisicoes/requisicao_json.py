import requests

url = 'https://viacep.com.br/ws/'
cep = input("Digite seu cep sem espaços ou barras: ")
formato = '/json/'

endpoint = url + cep + formato

resposta = requests.get(endpoint)
endereco= resposta.json()

if resposta.status_code == 200:
    print('Rua: ', endereco['logradouro'], '\nBairro: ', endereco['bairro'])
    print("")
else:
    print('Requisição inválida')