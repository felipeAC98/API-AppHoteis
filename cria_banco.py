import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()       #para efetuar selecoes

cria_tabela="CREATE TABLE IF NOT EXISTS hoteis (\
    hotel_id text PRIMARY  KEY,\
    nome text,\
    estrela real,\
    diaria real, \
    cidade text)"

cria_hotelA= "INSERT INTO hoteis VALUES (\
    'alpha','Alpha Hotel',4.3,420,'Sao Jose do Rio Preto')"

cria_hotelB= "INSERT INTO hoteis VALUES (\
    'bravo','bravo Hotel',4.8,730,'Sao Paulo')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotelA)
cursor.execute(cria_hotelB)

connection.commit()
connection.close()

