class HotelModel(): #herdando o modelo de banco

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