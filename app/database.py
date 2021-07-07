from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

def close_connection():
    db.session.close_all()

class Cidades(db.Model):
    __tablename__ = 'cidades'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(3), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    imagem_url = db.Column(db.String(255))
    alimentacao = db.Column(db.Text)
    hospedagem = db.Column(db.Text)
    #pontos_turisticos = db.relationship('Pontos_turisticos', back_populates="capitais", uselist=False)

    def __init__(self, estado, nome, descricao, imagem_url, alimentacao='', hospedagem=''):
        self.estado = estado
        self.nome = nome
        self.descricao = descricao
        self.imagem_url = imagem_url
        self.alimentacao = alimentacao
        self.hospedagem = hospedagem

    @staticmethod
    def read_all():
        var = Cidades.query.all()
        close_connection() 
        return var

    @staticmethod
    def read_single(cidade_id):
        close_connection()
        var = Cidades.query.get(cidade_id)
        close_connection()
        return var

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        close_connection()

    def update(self, new_data):
        self.estado = new_data.estado
        self.nome = new_data.nome
        self.descricao = new_data.descricao
        self.imagem_url = new_data.imagem_url
        self.alimentacao = new_data.alimentacao
        self.hospedagem = new_data.hospedagem
        self.save()
        close_connection()



class Pontos_turisticos(db.Model):
    __tablename__ = 'pontos_turisticos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text)
    id_cidade = db.Column(db.Integer, db.ForeignKey('cidades.id'), nullable=False)

    #capitais = db.relationship("Capitais", back_populates="pontos_turisticos")

    #imagens_url = db.relationship('Imagens_url', back_populates="pontos_turisticos", uselist=False)

    def __init__(self, nome, descricao, id_cidade):
        self.nome = nome
        self.descricao = descricao
        self.id_cidade = id_cidade

    @staticmethod
    def read_all():
        var = Pontos_turisticos.query.all()
        close_connection()
        return var

    @staticmethod
    def read_single(id_cidade):
        close_connection()
        var = Pontos_turisticos.query.get(id_cidade)
        close_connection()
        return var

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        close_connection()

    def update(self, new_data):
        self.nome = new_data.nome
        self.descricao = new_data.descricao
        self.id_cidade = new_data.id_cidade
        self.save()
        close_connection()

class Imagens_url(db.Model):
    __tablename__ = 'imagens_url'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    id_ponto_turistico = db.Column(db.Integer, db.ForeignKey('pontos_turisticos.id'))

    #pontos_turisticos = db.relationship('Pontos_turisticos', back_populates="imagens_url")

    def __init__(self, url, id_ponto_turistico):
        self.url = url
        self.id_ponto_turistico = id_ponto_turistico

    @staticmethod
    def read_all():
        var = Imagens_url.query.all()
        close_connection()
        return var

    @staticmethod
    def read_single(id_ponto_turistico):
        close_connection()
        var = Imagens_url.query.filter_by(id_ponto_turistico=id_ponto_turistico).first()
        close_connection()
        return var

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        close_connection()

    def update(self, new_data):
        self.url = new_data.url
        self.id_ponto_turistico = new_data.id_ponto_turistico
        self.save()
        close_connection()
