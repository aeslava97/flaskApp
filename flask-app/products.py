import datetime
def Products(cursor):
    cursor.execute("SELECT * FROM Product")
    data = cursor.fetchall()
    return data

def BuyProducts(cursor, idUser, idProduct): 
    cursor.execute("INSERT INTO Transaction(idUser, idProduct, date) VALUES({}, {}, '{}')".format(idUser,idProduct,datetime.datetime.today().strftime('%Y-%m-%d')))
