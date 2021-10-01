import requests
from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/vercep/<cep>', methods=['GET'])
def home (cep):
    url = 'https://viacep.com.br/ws/'
    formato= '/json/'

    request = requests.get(url + cep + formato)
    if (request.status_code == 200):
        return (request.json())
    else:
        return jsonify({"mensagem":"Requisição não encontrada"})

app.run(host='0.0.0.0', port=80)