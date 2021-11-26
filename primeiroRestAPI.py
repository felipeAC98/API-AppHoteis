from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis

app = Flask(__name__)
api = Api(app) 

api.add_resource(Hoteis,'/hoteis') #adicionando o recurso dentro da URI /hoteis

if __name__=='__main__':
    app.run(debug=True)