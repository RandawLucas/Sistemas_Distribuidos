import requests
url = 'https://viacep.com.br/ws/MG/Belo Horizonte/'
rua = []
end = []
formato = '/json/'
for x in range(0,2):
    rua.append(input('Digite o nome da rua: '))

for i in range(0,len(rua)):
    r = requests.get(url + rua[i] + formato)
    if (r.status_code == 200):
        print()
        print(r.json())
        print()
    else:
        print('Nao houve sucesso na requisicao.')