from flask_restful import Resource

#herdando a classe resource
class Santander(Resource):

    #todo resource possui get/post/...
    def get(self):
        return "Santander" #retornando um dict que ira ser convertido para json
