from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

from datetime import date

import sqlite3
from sqlite3 import Error


#######################################################
# Instancia da Aplicacao Flask

app = Flask(__name__)


#######################################################

# 1. Cadastrar produtos
@app.route('/produtos/cadastrar', methods=['GET', 'POST'])

def cadastrar():

    if request.method == 'POST':

        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        datacriacao = date.today()

        mensagem = 'Erro - nao cadastrado'

        if descricao and precocompra and precovenda and datacriacao:
            registro = (descricao, precocompra, precovenda, datacriacao)

            try:
                conn = sqlite3.connect('database/db-produtos.db')

                sql = ''' INSERT INTO produtos(descricao, precocompra, precovenda, datacriacao)
                              VALUES(?,?,?,?) '''

                cur = conn.cursor()

                cur.execute(sql, registro)

                conn.commit()

                mensagem = 'Sucesso - cadastrado'
                print(mensagem)

            except Error as e:
                print(e)
            finally:
                conn.close()

        print(mensagem)
    return render_template('cadastrar.html')


#######################################################

# 2. Listar produtos
@app.route('/produtos/listar', methods=['GET'])

def listar():
    try:
        conn = sqlite3.connect('database/db-produtos.db')

        sql = '''SELECT * FROM produtos'''

        cur = conn.cursor()

        cur.execute(sql)

        registros = cur.fetchall()

        return render_template('listar.html', regs=registros)

    except Error as e:
        print(e)
    finally:
        conn.close()

#######################################################

# rota deletar
@app.route('/produtos/deletar/<int:codproduto>', methods=['DELETE'])

def deletar(codproduto=None):
    if codproduto == None:
        return jsonify({'menssagem': 'parametro invalido'})
    else:
        try:
            conn = sqlite3.connect('database/db-produtos.db')

            sql = '''DELETE FROM produtos WHERE codproduto = ''' + str(codproduto)

            cur = conn.cursor()
            cur.execute(sql)

            conn.commit()

            return jsonify({"menssagem": 'registro excluido'})

        except Error as e:
            return jsonify({'menssagem': e})
        finally:
            conn.close()

#######################################################

# Rota de Alteração de dados
@app.route('/produtos/alterar/<int:codproduto>', methods=['PUT'])

def alterar(codproduto=None):
    campo = 'precovenda'
    valor = 3
    if codproduto == None:
        return jsonify({'mensagem': 'parametro invalido'})
    else:
        try:
            conn = sqlite3.connect('database/db-produtos.db')

            sql = '''UPDATE produtos SET '''+str(campo)+'''='''+str(valor)+''' WHERE codproduto =''' + str(codproduto)

            cur = conn.cursor()
            cur.execute(sql)

            conn.commit()

            return jsonify({"menssagem": 'registro alterado'})

        except Error as e:
            return jsonify({'menssagem': e})

#######################################################

# Rota de Erro
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404



#######################################################
# Execucao da Aplicacao

if __name__ == '__main__':
    app.run()

