from sql_alchemy import banco

class HotelModel(banco.Model): #herdando o modelo de banco

    __tablename__ = 'hoteis' #necessario para nomear a tabela no SQL_alchemy

    hotel_id=banco.Column(banco.String, primary_key=True) #definindo que a variavel hotel_id sera uma string e do tipo [prymary key]
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1)) #numeros de casa depois da virgula
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id=hotel_id
        self.nome=nome
        self.estrelas=estrelas
        self.diaria=diaria
        self.cidade=cidade

    #funcao de conversao do objeto para formato json(dict)
    def json(self):
        return {
            'hotel_id':self.hotel_id,
            'nome':self.nome,
            'estrelas':self.estrelas,
            'diaria':self.diaria,
            'cidade':self.cidade            
        }