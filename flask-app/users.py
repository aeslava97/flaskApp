def getUser(cursor, idUser):
    cursor.execute("SELECT * FROM User WHERE NAME = {}".format(idUser))
    data = cursor.fetchall()
    return data