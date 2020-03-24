def getUser(cursor, idUser):
	sql = "SELECT * FROM User WHERE name = %s"
	val = (idUser)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return data

def getCupon(cursor, idUser):
	sql = "SELECT * FROM CuponExtra WHERE idUser = %s"
	val = (idUser)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return data

def validateUser(cursor, idUser, passw):
	sql = "SELECT * FROM User WHERE name = %s AND password = %s"
	val = (idUser, passw)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return len(data) != 0