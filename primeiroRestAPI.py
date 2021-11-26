from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app) 

#o primeiro parametro eh referente a classe que sera invocada
api.add_resource(Hoteis,'/hoteis') #adicionando o recurso dentro da URI /hoteis
api.add_resource(Hotel,'/hoteis/<string:hotel_id>') #adicionando o recurso dentro da URI /hoteis

if __name__=='__main__':
    app.run(debug=True)