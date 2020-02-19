def getHistory(cursor, idUser):
    cursor.execute("SELECT * FROM Transaction WHERE idUser = {}".format(idUser))
    data = cursor.fetchall()
    return data