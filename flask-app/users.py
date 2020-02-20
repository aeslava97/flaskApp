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