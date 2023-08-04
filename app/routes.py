from app import app
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato
import time 

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title ='Sobre')

@app.route('/contato',methods=['GET','POST'])
def contato():
    dados_formulario = None
    formulario = Contato()
    if request.method == 'POST':
        flash('Seu formulario foi enviado com sucesso')
        #time.sleep(2)
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        conteudo = request.form.get('conteudo')
        #return redirect('/contato')
    
        dados_formulario = {
            'nome':nome,
            'email':email,
            'telefone':telefone,
            'conteudo':conteudo,
        }
    return render_template('contato.html', title ='Contato', formulario = formulario, dados_formulario = dados_formulario)


@app.route('/projetos')
def projeto():
    return render_template('projeto.html', title ='Projetos')

