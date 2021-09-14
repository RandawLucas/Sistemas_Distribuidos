import requests
r = requests.get('https://viacep.com.br/abc/"')
print(r.status_code)
print(r.text)
