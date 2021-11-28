from flask_restful import Resource , reqparse
from models.hotel import HotelModel

hoteis = [
{
    'hotel_id':'alpha',
    'nome':'Alpha Hotel',
    'estrelas':4.3,
    'diaria':420,
    'cidade':'Sao Jose do Rio Preto'
},
{
    'hotel_id':'bravo',
    'nome':'bravo Hotel',
    'estrelas':4.8,
    'diaria':730,
    'cidade':'Sao Paulo'
},
{
    'hotel_id':'charlie',
    'nome':'charlie Hotel',
    'estrelas':3.3,
    'diaria':50,
    'cidade':'Bady Bassitt'
}
]

#mesma lista de cima porem em forma de dicionario para ter uma busca O1 quando for relacionada ao ID do hotel
hoteis_O1 = {
    'hotel_id':{
        'alpha':{
            'hotel_id':'alpha',
            'nome':'Alpha Hotel',
            'estrelas':4.3,
            'diaria':420,
            'cidade':'Sao Jose do Rio Preto'
        },
        'bravo':{
            'hotel_id':'bravo',
            'nome':'bravo Hotel',
            'estrelas':4.8,
            'diaria':730,
            'cidade':'Sao Paulo'
         },
        'charlie':{
            'hotel_id':'charlie',
            'nome':'charlie Hotel',
            'estrelas':3.3,
            'diaria':50,
            'cidade':'Bady Bassitt'
         },        
    }
}

#herdando a classe resource
class Hoteis(Resource):

    #todo resource possui get/post/...
    def get(self):
        #cada retorno da query eh um objeto do tipo HotelModel
        #SELECT * FROM HOTEIS
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}#retornando um dict que ira ser convertido para json

class Hotel(Resource):
    #atributos de um hotel (um pouco estranho ver dessa forma mas faz sentido) (eles so sao chamados mesmo quando chamamos o parse_args)
    argumentos= reqparse.RequestParser()
    #somente os argumentos definidos abaixo sao aceitos no post
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def adicionaHotel(self, novoHotel):
        #adicionando no dict do hotel
        hoteis_O1['hotel_id'][novoHotel['hotel_id']]=novoHotel
        #adicionando tambem na lista de hoteis
        hoteis.append(novoHotel)

    def get(self, hotel_id):
        hotel=HotelModel.find_hotel(hotel_id)
        if hotel :
            return hotel.json()
        return {'message':'Hotel id not found'},404 #padrao para retorno de erros
        pass

    #POST- Para criar algo novo
    #o segundo argumento eh provindo da URI
    def post(self, hotel_id):

        #verificando se o hotel id ja existe
        if HotelModel.find_hotel(hotel_id): #utilizando uma funcao da classe(cls) para efetuar a busca no banco
            return {"message": "Hotel ID '{}' already exists.".format(hotel_id)},400

        #recebendo os valores para uma variavel no formato dict
        dadosRecebidos = self.argumentos.parse_args()

        #passando os kargs como argumento (dadosRecebidos eh um dict) da classe HotelModel e entao instanciando um objeto da classe hotelModel
        novo_hotel=HotelModel(hotel_id, **dadosRecebidos)

        try:
            #chamando a funcao save_hotel
            novo_hotel.save_hotel()
        except:
            return {'message':'An internal error ocurred trying to save hotel'}, 500 #500 eh internal server error
        return novo_hotel.json()
    
    #PUT - Para atualizar alguma informacao de algum campo (ainda assim precisa receber todos valores, inclusive aqueles que nao serao alterados)
    def put(self,hotel_id):

        #obtendo dados
        dadosRecebidos = self.argumentos.parse_args()
        hotel_existente=HotelModel.find_hotel(hotel_id)

        #caso ohotel ja exista vamos somente atualizar os dados dele
        if hotel_existente :
            hotel_existente.update_hotel(**dadosRecebidos)
            hotel_existente.save_hotel() #salvando a alteracao feita no objeto para o banco
            return hotel_existente.json(), 200

        else:
            novo_hotel =HotelModel(hotel_id, **dadosRecebidos)
        try:
            #chamando a funcao save_hotel
            novo_hotel.save_hotel()
        except:
            return {'message':'An internal error ocurred trying to save hotel'}, 500 #500 eh internal server error
        return novo_hotel.json(), 201 #novo codigo para indicar que o hotel foi criado

    def delete(self,hotel_id):

        hotel_existente=HotelModel.find_hotel(hotel_id)
        if hotel_existente :
            try:
                hotel_existente.delete_hotel()
            except:
                 return {'message':'An error ocurred trying to delete'}, 500
            return {'message':'Hotel deleted'}, 200 #novo codigo para indicar que o hotel foi criado
        
        return {'message':'Hotel ID was not found'}, 400
        pass    #para nao precisar implementar o codigo ainda
    