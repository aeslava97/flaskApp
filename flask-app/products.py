def Products(cursor):
    cursor.execute("SELECT * FROM Product")
    data = cursor.fetchall()
    return data