import requests
url = 'https://viacep.com.br/ws/'
cep = input('Digite o  CEP: ')

formato = '/xml/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print()
    print('JSON : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')