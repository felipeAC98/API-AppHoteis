from flask_restful import Resource , reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp

atributos=reqparse.RequestParser()
atributos.add_argument('login',type=str,required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha',type=str,required=True, help="The field 'senha' cannot be left blank")


class User(Resource):
    #/usuarios/{user_id}

    def get(self, user_id):
        user=UserModel.find_user(user_id)
        if user :
            return user.json()
        return {'message':'User id not found'},404 #padrao para retorno de erros
        pass
    
    @jwt_required()
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
        dados=atributos.parse_args()    

        #Verificando se o usuario ja existe
        if UserModel.find_by_login(dados['login']):
            return {"message":"Login '{}' alread exists".format(dados['login'])}

        user=UserModel(**dados)
        user.save_user()
        return {"message":'User created successfully'} ,201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados=atributos.parse_args()  

        user=UserModel.find_by_login(dados['login'])

        #as funcoes abaixo sao provindas do PyJWT e do proprio python
        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso= create_access_token(identity=user.user_id)
            return{'access_token':token_de_acesso},200

        return {'message':'The username or password is incorrect.'},401