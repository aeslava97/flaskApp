def Products(cursor):
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    products = [
        {
            'id': 1,
            'name': 'articulo1',
            'body': 'loremloremlorem',
            'precio': 50000,
            'date': '03-11-1997'
        },{
            'id': 2,
            'name': 'articulo2',
            'body': 'loremloremlorem',
            'precio': 100000,
            'date': '04-11-1997'
        }
    ]
    return products