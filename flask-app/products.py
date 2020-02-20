import datetime
def Products(cursor):
	cursor.execute("SELECT * FROM Product")
	data = cursor.fetchall()
	return data

def BuyProducts(cursor, idUser, idProduct, wallet, value):
	sql = "INSERT INTO Transaction(idUser, idProduct, date) VALUES(%s, %s, %s)"
	val = (idUser,idProduct,datetime.datetime.today().strftime('%Y-%m-%d'))
	sql1 = "UPDATE User SET Wallet = %s, WASTED = %s WHERE NAME = %s"
	val1 = (wallet-value,value,idUser)
	cursor.execute(sql, val)
	cursor.execute(sql1, val1)

def getProduct(cursor, id):
	sql = "SELECT * FROM Product WHERE ID = %s"
	val = (id)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return data