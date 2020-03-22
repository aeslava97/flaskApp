def getHistory(cursor, idUser):
	sql = "SELECT * FROM Transaction WHERE idUser = %s"
	val = (idUser)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return data

def getFirstHistory(cursor, idUser):
	sql = "SELECT id FROM Transaction WHERE idUser = %s ORDER BY date ASC LIMIT 1 "
	val = (idUser)
	cursor.execute(sql, val)
	data = cursor.fetchall()
	return data