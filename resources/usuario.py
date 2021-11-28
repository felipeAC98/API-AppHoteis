from flask_restful import Resource , reqparse
from models.usuario import UserModel

class User(Resource):
    #/usuarios/{user_id}

    def get(self, user_id):
        user=UserModel.find_user(user_id)
        if user :
            return user.json()
        return {'message':'User id not found'},404 #padrao para retorno de erros
        pass
    
    def delete(self,user_id):

        user=UserModel.find_user(user_id)
        if user :
            try:
                user.delete_user()
            except:
                 return {'message':'An error ocurred trying to delete'}, 500
            return {'message':'User deleted'}, 200 #novo codigo para indicar que o hotel foi criado
        
        return {'message':'User ID was not found'}, 400
        pass    #para nao precisar implementar o codigo ainda

#Criando uma nova classe para tratar do outro endpoit (cadastro)
class UserRegister(Resource):

    def post(self):
        atributos=reqparse.RequestParser()
        atributos.add_argument('login',type=str,required=True, help="The field 'login' cannot be left blank")
        atributos.add_argument('senha',type=str,required=True, help="The field 'senha' cannot be left blank")

        dados=atributos.parse_args()    

        #Verificando se o usuario ja existe
        if UserModel.find_by_login(dados['login']):
            return {"message":"Login '{}' alread exists".format(dados['login'])}

        user=UserModel(**dados)
        user.save_user()
        return {"message":'User created successfully'} ,201
