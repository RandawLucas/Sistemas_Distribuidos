import requests
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

if (r.status_code == 200):
    print()
    print('Retorno : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')

with open('gravacao.txt', 'w') as gravacao:
    gravacao.write(r.text)