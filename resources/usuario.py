from flask_restful import Resource , reqparse
from models.usuario import UserModel

class User(Resource):

    def get(self, user_id):
        user=UserModel.find_hotel(user_id)
        if user :
            return user.json()
        return {'message':'User id not found'},404 #padrao para retorno de erros
        pass
    
    def delete(self,hotel_id):

        user=UserModel.find_user(hotel_id)
        if user :
            try:
                user.delete_user()
            except:
                 return {'message':'An error ocurred trying to delete'}, 500
            return {'message':'User deleted'}, 200 #novo codigo para indicar que o hotel foi criado
        
        return {'message':'User ID was not found'}, 400
        pass    #para nao precisar implementar o codigo ainda
    