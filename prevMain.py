from flask import Flask, render_template, redirect, request, url_for, flash
import pandas as pd

app = Flask(__name__)

##Página de entrada para ver a tabela de usuarios.
@app.route('/')
def index():
    with open('tabela_ipca_teto.html','r') as f:
        dados = f.read()
    return render_template('index.html', tbl_dados = dados)


##Método main para rodar app.
if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)