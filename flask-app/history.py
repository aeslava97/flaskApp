def getHistory(cursor, idUser):
	sql = "SELECT * FROM Transaction WHERE idUser = %s"
	val = (idUser)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return data