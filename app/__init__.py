from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.session import close_all_sessions

app = Flask(__name__)

# DATABASE
user = 'nuifpqap'
password = 'EBK9sJXl0RWoWh8cjZjRo7vw4bZ0MWjA'
host = 'tuffi.db.elephantsql.com'
database = 'nuifpqap'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.database import Cidades, Pontos_turisticos, Imagens_url, close_connection

@app.route('/')
def index():
    close_connection()
    cidades = Cidades.read_all()
    pontos_turisticos = Pontos_turisticos.read_all()
    imagens_url = Imagens_url.read_all()
    
    return render_template('index.html', cidades=cidades, pontos_t=pontos_turisticos, imagens_url=imagens_url)
    
@app.route('/<id_ponto_t>')
def saiba_mais(id_ponto_t):
    close_connection()
    ponto_t = Pontos_turisticos.read_single(id_ponto_t)
    
    imagens = Imagens_url.query.filter_by(id_ponto_turistico=id_ponto_t).all()
    cidade = Cidades.read_single(ponto_t.id_cidade)
    
    return render_template('pt.html', ponto_t=ponto_t, imagens=imagens, cidade=cidade)

@app.route('/create', methods=['GET', 'POST'])
def create():
    close_connection()
    sucesso = False

    if request.method == 'POST':
        form = request.form

        cidade = Cidades(form['estado'], form['cidade'], form['imagem_url'], form['alimentacao'], form['hospedagem'])
        cidade.save()
    
        ponto_turistico = Pontos_turisticos(form['nome-ponto_turistico'], form['descricao-ponto_turistico'], cidade.id)
        ponto_turistico.save()

        imagem_url = Imagens_url(form['url_imagem-ponto_turistico'], ponto_turistico.id)
        imagem_url.save()
        close_connection()
        sucesso = True

    
    return render_template('create.html', sucesso=sucesso)

@app.route('/update/<cidade_id>', methods=['GET', 'POST'])
def update(cidade_id):
    sucess = False 
    cidade = Cidades.read_single(cidade_id)
    ponto_turistico = Pontos_turisticos.read_single(cidade_id)
    ponto_id = ponto_turistico.id
    imagem_url = Imagens_url.read_single(ponto_turistico.id)
    

    if request.method == 'POST':
    
        form = request.form

        if form.get('delete') == None:
            new_data = Cidades(form['estado'], form['cidade'], form['imagem_url'], form['alimentacao'], form['hospedagem'])
            cidade.update(new_data)
            
            new_data = Pontos_turisticos(form['nome-ponto_turistico'], form['descricao-ponto_turistico'], cidade_id)
            ponto_turistico.update(new_data)
            new_data = Imagens_url(form['url_imagem-ponto_turistico'], ponto_id)
            imagem_url.update(new_data)

            sucess = True
        else:
            imagem_url.delete()
            ponto_turistico.delete()
            cidade.delete()
            
            sucess = 2

    return render_template('update.html', sucesso=sucess, cidade=cidade, ponto_t=ponto_turistico, imagem_url=imagem_url)

@app.route('/sobre')
def sobre():
    close_connection()
    return render_template('sobre.html')

@app.route('/motivacao')
def motivacao():
    close_connection()
    return render_template('motivacao.html')

@app.route('/contato')
def contato():
    close_connection()
    return render_template('contato.html')


