from flask import Flask
from flask_restful import Api
from resources.bancos import Santander

app = Flask(__name__)
api = Api(app) 

api.add_resource(Santander,'/') #adicionando o recurso dentro da URI /hoteis

if __name__=='__main__':
    app.run(debug=True)