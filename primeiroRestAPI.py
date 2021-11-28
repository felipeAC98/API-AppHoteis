from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)                                       #o app do tipo flask
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///banco.db' #para criar na raiz do diretorio um banco do tipo sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False         #para evitar o aviso de alteracao
app.config['JWT_SECRET_KEY']='213knfsldr13'                 #definindo a chave de criptografia
api = Api(app) 
jwt = JWTManager(app) #para tratar das questoes de autenticacao do app

@app.before_first_request
def cria_banco():
    banco.create_all() #criando o banco e tabelas antes da primeira requisicao

#o primeiro parametro eh referente a classe que sera invocada
api.add_resource(Hoteis,'/hoteis') #adicionando o recurso dentro da URI /hoteis
api.add_resource(Hotel,'/hoteis/<string:hotel_id>') #adicionando o recurso dentro da URI /hoteis

api.add_resource(User,'/usuarios/<int:user_id>') #adicionando o recurso dentro da URI /usuarios
api.add_resource(UserRegister,'/cadastro') #adicionando o recurso dentro da URI /cadastro
api.add_resource(UserLogin,'/login') #adicionando o recurso dentro da URI /login

if __name__=='__main__':
    from sql_alchemy import banco 
    banco.init_app(app) 
    app.run(debug=True)