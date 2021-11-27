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
        return {'hoteis': hoteis_O1}#retornando um dict que ira ser convertido para json

class Hotel(Resource):
    #atributos de um hotel (um pouco estranho ver dessa forma mas faz sentido) (eles so sao chamados mesmo quando chamamos o parse_args)
    argumentos= reqparse.RequestParser()
    #somente os argumentos definidos abaixo sao aceitos no post
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def adicionaHotel(self, novoHotel):
        #adicionando no dict do hotel
        hoteis_O1['hotel_id'][novoHotel['hotel_id']]=novoHotel
        #adicionando tambem na lista de hoteis
        hoteis.append(novoHotel)

    def get(self, hotel_id):
        hotel=self.findHotel(hotel_id)
        if hotel :
            return hotel
        return {'message':'Hotel id not found'},404 #padrao para retorno de erros
        
        pass

    #o segundo argumento eh provindo da URI
    def post(self, hotel_id):

        #verificando se o hotel id ja existe
        if HotelModel.find_hotel(hotel_id): #utilizando uma funcao da classe(cls) para efetuar a busca no banco
            return {"message": "Hotel ID '{}' already exists.".format(hotel_id)},400

        #recebendo os valores para uma variavel no formato dict
        dadosRecebidos = self.argumentos.parse_args()

        #passando os kargs como argumento (dadosRecebidos eh um dict) da classe HotelModel e entao instanciando um objeto da classe hotelModel
        novo_hotel=HotelModel(hotel_id, **dadosRecebidos)

        #chamando a funcao save_hotel
        novo_hotel.save_hotel()
        return novo_hotel.json()
     
    def put(self,hotel_id):

        #obtendo dados
        dadosRecebidos = self.argumentos.parse_args()
        novo_hotel =HotelModel(hotel_id, **dadosRecebidos).json()
        # o codigo acima faz o mesmo que este de baixo porem de uma forma mais eficiente
        '''
            novo_hotel ={
                'hotel_id':hotel_id,
                'nome':dadosRecebidos['nome'],
                'estrelas':dadosRecebidos['estrelas'],
                'diaria':dadosRecebidos['diaria'],
                'cidade':dadosRecebidos['cidade']
            }
        '''

        hotel=self.findHotel(hotel_id)
        if hotel :
            hotel.update(novo_hotel)
            return novo_hotel, 200

        else:
            self.adicionaHotel(novo_hotel)
            return novo_hotel, 201 #novo codigo para indicar que o hotel foi criado

    def delete(self,hotel_id):
        global hoteis
        hoteis=[hotel for hotel in hoteis if hotel['hotel_id'] !=hotel_id]
        return {'message':'Hotel deleted'}, 200 #novo codigo para indicar que o hotel foi criado
        pass    #para nao precisar implementar o codigo ainda
    