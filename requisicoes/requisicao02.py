import requests
url = 'https://viacep.com.br/ws/'
cep = []
formato = '/xml/'
for x in range(0,5):
    cep.append(input('Digite o  CEP: '))
for i in range(0,len(cep)):
    r = requests.get(url + cep[i] + formato)
    if (r.status_code == 200):
        print()
        print('JSON : ', r.text)
        print()
    else:
        print('Nao houve sucesso na requisicao.')