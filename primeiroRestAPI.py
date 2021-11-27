from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)                                       #o app do tipo flask
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///banco.db' #para criar na raiz do diretorio um banco do tipo sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False         #para evitar o aviso de alteracao
api = Api(app) 

@app.before_first_request
def cria_banco():
    banco.create_all() #criando o banco e tabelas antes da primeira requisicao

#o primeiro parametro eh referente a classe que sera invocada
api.add_resource(Hoteis,'/hoteis') #adicionando o recurso dentro da URI /hoteis
api.add_resource(Hotel,'/hoteis/<string:hotel_id>') #adicionando o recurso dentro da URI /hoteis

if __name__=='__main__':
    from sql_alchemy import banco 
    banco.init_app(app) 
    app.run(debug=True)