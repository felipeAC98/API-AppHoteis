from sql_alchemy import banco

class UserModel(banco.Model): #herdando o modelo de banco

    __tablename__ = 'usuarios' #necessario para nomear a tabela no SQL_alchemy

    user_id=banco.Column(banco.Integer, primary_key=True) #definindo que a variavel hotel_id sera uma string e do tipo [prymary key]
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha):
        #o ID nao eh recebido como parametro, sendo assim o SQL_alchemy ira criar automaticamente um valor para ele quando um novo objeto for criado pois ele eh primary key
        self.login=login
        self.senha=senha

    #funcao de conversao do objeto para formato json(dict)
    def json(self):
        return {
            'user_id':self.user_id,
            'login':self.login    
            #nao vamos enviar a senha quando formos retornar o json    
        }

    @classmethod
    def find_user(cls, user_id):

        #select * from user u where u.user_id = $user_id 
        user= cls.query.filter_by(user_id=user_id).first() #o metodo query eh da classe que extendemos

        if user:
            return user
        else:
            return None

    @classmethod
    def find_by_login(cls, login):

        #select * from user u where u.login = $login 
        user= cls.query.filter_by(login=login).first() #o metodo query eh da classe que extendemos

        if user:
            return user
        else:
            return None

    def save_user(self):
        #salvando os atributos da classe hotel recebidos como uma nova linha do banco
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        #salvando os atributos da classe hotel recebidos como uma nova linha do banco
        banco.session.delete(self)
        banco.session.commit()   