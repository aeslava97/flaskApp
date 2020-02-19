import datetime
def Products(cursor):
    cursor.execute("SELECT * FROM Product")
    data = cursor.fetchall()
    return data

def BuyProducts(cursor, idUser, idProduct, wallet, value):
    cursor.execute("INSERT INTO Transaction(idUser, idProduct, date) VALUES({}, {}, '{}')".format(idUser,idProduct,datetime.datetime.today().strftime('%Y-%m-%d')))
    cursor.execute("UPDATE User SET Wallet = {}, WASTED = {} WHERE NAME = {}".format(wallet-value,value,idUser))

def getProduct(cursor, id):
    cursor.execute("SELECT * FROM Product WHERE ID = {}".format(id))
    data = cursor.fetchall()
    return data