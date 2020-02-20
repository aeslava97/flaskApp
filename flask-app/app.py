#!/usr/bin/env/python3.6
from flask import Flask, request, redirect, url_for, Markup, make_response, flash, abort
from flaskext.mysql import MySQL
from jinja2 import Environment, FileSystemLoader
import subprocess
from http import cookies
from random import randint
from products import Products, BuyProducts, getProduct
from users import getUser
from users import getCupon
from history import getHistory
from flask.templating import render_template
import sys


app = Flask(__name__)
app.secret_key = "super secret key"
loader = FileSystemLoader( searchpath="templates/" )
env = Environment(loader=loader)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_SOCKET'] = None





mysql = MySQL()
mysql.init_app(app)
usuarioActual = "hola"
print("------------usuarioActual-------------")
print(usuarioActual)
print("------------usuarioActual-------------")
@app.route('/', methods=['GET', 'POST','PUT'])
def logins():        
    if request.method == "POST" and ("user" in request.form.keys()) and ("password" in request.form.keys()):
        details = request.form
        user = details['user']
        usuarioActual = user
        password = details['password']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS User ("
                            "name VARCHAR(100) NOT NULl,"
                            "PRIMARY KEY(name),"
                            "Wallet FLOAT,"
                            "password  VARCHAR(100),"
                            "Wallet FLOAT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Product ("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "PRIMARY KEY(id),"
                            "name    VARCHAR(100),"
                            "value    FLOAT,"
                            "Description  VARCHAR(100),"
                            "img    VARCHAR(100))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Transaction ("
                            "idUser VARCHAR(100) NOT NULL ,"
                            "FOREIGN KEY (idUser) REFERENCES User(name),"
                            "idProduct INT NOT NULL ,"
                            "FOREIGN KEY (idProduct) REFERENCES Product(id),"
                            "date  DATETIME)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Cupon ("
                            "idCupon INT NOT NULL AUTO_INCREMENT,"
                            "PRIMARY KEY(idCupon),"
                            "idUser    VARCHAR(100) NOT NULL,"
                            "FOREIGN KEY (idUser) REFERENCES User(name),"
                            "valueMoney    FLOAT)")
        # cont = 6
        # while cont != 0:
        #     sql4 = "INSERT INTO Product(id, name, value, Description , img) VALUES (%s, %s, %s, %s, %s)"
        #     val4 = (cont, "Producto"+ str(cont), 50+ cont, "Un muy buen producto", "https://cdn2.iconfinder.com/data/icons/e-commerce-line-4-1/1024/open_box4-512.png")
        #     cursor.execute(sql4, val4)
        #     cont = cont - 1
        sql2 = "SELECT * from User WHERE  name = %s AND password = %s"
        val2 = (user, password)
        cursor.execute(sql2, val2)
        conn.commit()
        cursor.close()
        data = cursor.fetchall() 
        if data:
            resp = make_response(redirect('/home'))
            resp.set_cookie('user', user)
            return resp
        else:
            return redirect('/')

    elif request.method == "POST" and request.form['userR'] != "" and request.form['passwordR'] != "":
        details1 = request.form
        user1 = details1['userR']
        usuarioActual = user1
        password1 = details1['passwordR']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS User ("
                            "name VARCHAR(100) NOT NULl,"
                            "PRIMARY KEY(name),"
                            "Wallet FLOAT,"
                            "password  VARCHAR(100),"
                            "wasted FLOAT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Product ("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "PRIMARY KEY(id),"
                            "name    VARCHAR(100),"
                            "value    FLOAT,"
                            "Description  VARCHAR(100),"
                            "img    VARCHAR(100))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Transaction ("
                            "idUser VARCHAR(100) NOT NULL ,"
                            "FOREIGN KEY (idUser) REFERENCES User(name),"
                            "idProduct INT NOT NULL ,"
                            "FOREIGN KEY (idProduct) REFERENCES Product(id),"
                            "date  DATETIME)")
        cursor.execute("CREATE TABLE IF NOT EXISTS CuponExtra ("
                            "idCupon INT NOT NULL ,"
                            "PRIMARY KEY(idCupon),"
                            "idUser    VARCHAR(100) NOT NULL,"
                            "FOREIGN KEY (idUser) REFERENCES User(name),"
                            "valueMoney     VARCHAR(100) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS CuponValido ("
                            "idCupon INT NOT NULL ,"
                            "PRIMARY KEY(idCupon),"
                            "activo  INT NOT NULL)")
        conn.commit()
        cursor.close()
        cursor = conn.cursor()
        sql1 = "SELECT * from User WHERE  name = %s AND password = %s"
        val1 = (user1, password1)
        cursor.execute(sql1, val1)
        conn.commit()
        cursor.close()
        data11 = cursor.fetchall() 
        if data11:
            return redirect('/')
        else:
            cursor = conn.cursor()
            sql = "INSERT INTO User(name, Wallet, password, wasted) VALUES (%s, %s, %s, %s)"
            val = (user1, 0, password1, 0)
            cursor.execute(sql, val)
            idRand = randint(1, 1000)
            sql3 = "INSERT INTO CuponExtra(idCupon, idUser, valueMoney)VALUES (%s, %s, %s)"
            val3 = (str(idRand), user1, 100)
            
            cursor.execute(sql3, val3)
            sql4 = "INSERT INTO CuponValido(idCupon,activo)VALUES (%s,%s)"
            val4 = (str(idRand),1)
            cursor.execute(sql4, val4)
            
            conn.commit()
            cursor.close()
            resp = make_response(redirect('/home'))
            resp.set_cookie('user', user1)
            return resp
            
    # return "login and register"
    template = env.get_template('logins.html')
    return make_response(template.render())

@app.route('/home' , methods=['GET', 'POST'])
def show_home():
    conn = mysql.connect()
    cursor = conn.cursor()
    data = getUser(cursor,request.cookies['user'])
    data1 = getCupon(cursor,request.cookies['user'])
    details = request.form  
    if request.method == "POST" and ("cupon" in request.form.keys()) and ("amount" in request.form.keys()):   
        idCuponNuevo=details['cupon']  
        saldoSolicitado=details['amount']     
        args = ("gcc","-o","static/binario $(mysql_config --cflags) static/script.c $(mysql_config --libs)")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        
    
        args = ("static/binario",idCuponNuevo)
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        
        outputnuevo=output.decode(encoding='utf-8', errors='strict')
        print("*****************************", file=sys.stderr)
        print(outputnuevo+"+++++++++++++", file=sys.stderr)
       #Si es 1 el cupon es valido si es 0 no es valido
        if(int(str(outputnuevo))==1):
            
            conn = mysql.connect()
            cursor = conn.cursor()
            
            sql= "SELECT  valueMoney FROM  CuponExtra WHERE idCupon = %s "
            valoresCupon=(int(idCuponNuevo))
            cursor.execute(sql,valoresCupon)
            data = cursor.fetchone()
            
            #Dinero bono
            saldoDisponible= int(str(data[0]))
            #Modifico el saldo de acuerdo a la  cantidad solicitada
            if(int(saldoSolicitado)<=saldoDisponible):
                
                #Actualizo el nuevo saldo del cupon disponible en en la base de datos
                saldoNuevo=saldoDisponible-int(saldoSolicitado)
                sqlActualizacionSaldo = "UPDATE CuponExtra SET valueMoney = %s WHERE idCupon = %s "
                valoresActualizacion = (saldoNuevo, int(idCuponNuevo))
                cursor.execute(sqlActualizacionSaldo, valoresActualizacion)
                
                #Actualizo saldo usuario agrego dinero a su wallet
                dataUsuarioActual = getUser(cursor,request.cookies['user'])
                
                #Busco el wallet del usuario actual
                sqlWalletActual= "SELECT  Wallet FROM  User WHERE +" "name= %s "
                usuarioActual = (str(dataUsuarioActual[0][0]))
                cursor.execute(sqlWalletActual,usuarioActual)
                dataWalletActual = cursor.fetchone()
                
                #Nuevo saldo Wallet total
                saldoNuevoTotal= (dataWalletActual[0])+ float(saldoSolicitado)
        
                #Actualizo perfil de usuario
                sqlActualizacionWallet = "UPDATE User SET Wallet = %s WHERE "+ "name = %s "
                valoresActualizacionUsuario = (str(saldoNuevoTotal),str(dataUsuarioActual[0][0]))
                cursor.execute(sqlActualizacionWallet, valoresActualizacionUsuario)
                mensajeTransaccion='Your wallet has been updated !!!'
                conn.commit()
                conn.close() 
                connectionPerfil = mysql.connect()
                connection = mysql.connect()
                cursor = connection.cursor()
                data = getUser(cursor,request.cookies['user'])
                dataCupon = getCupon(cursor,request.cookies['user'])
                cursor.close() 
                return render_template('home.html',profile = data, cupons = dataCupon, mensajePositivo=mensajeTransaccion)    
             #Desactivo cupon si no tiene fondos   
            if saldoDisponible==0:
                mensajeTransaccion="There is no more money in your cupon"
                sqlDesactivoCupon = "UPDATE CuponValido SET activo = %s WHERE idCupon = %s "
                valoresDeCupoAdesactivar=(0,int(idCuponNuevo))
                cursor.execute(sqlDesactivoCupon, valoresDeCupoAdesactivar)
                conn.commit()
                conn.close()
                connectionPerfil = mysql.connect()
                connection = mysql.connect()
                cursor = connection.cursor()
                data = getUser(cursor,request.cookies['user'])
                dataCupon = getCupon(cursor,request.cookies['user'])
                cursor.close() 
                return render_template('home.html',profile = data, cupons = dataCupon, mensaje=mensajeTransaccion)
            else :
                mensajeTransaccion="You do not have enough funds"
                connectionPerfil = mysql.connect()
                connection = mysql.connect()
                cursor = connection.cursor()
                data = getUser(cursor,request.cookies['user'])
                dataCupon = getCupon(cursor,request.cookies['user'])
                cursor.close() 
                return render_template('home.html',profile = data, cupons = dataCupon, mensaje=mensajeTransaccion)

    cursor.close()
    return render_template('home.html',profile = data, cupons = data1)

@app.route('/products' , methods=['GET', 'POST'])
def products():
    conn = mysql.connect()
    cursor = conn.cursor()
    data = Products(cursor)
    cursor.close()
    return render_template('products.html',products = data)

@app.route('/products/buying/<id>', methods=['POST'])
def buying(id):
    user = request.cookies['user']
    conn = mysql.connect()
    cursor = conn.cursor()
    productData = getProduct(cursor,id)[0]
    userData  = getUser(cursor,user)[0]
    wallet = userData[1]
    value = productData[2]
    wasted = userData[3]
    if wallet >= value:
        BuyProducts(cursor, user, id, wallet, value, wasted)
        conn.commit()
        cursor.close()
        return ('', 204)
    abort(409)

@app.route('/history' , methods=['GET'])
def show_history():
    user = request.cookies['user']
    conn = mysql.connect()
    cursor = conn.cursor()
    data = getHistory(cursor, user)
    cursor.close()
    return render_template('history.html',histories = data)          


@app.route('/hello/<name>')
def hello(name):
    template = env.get_template('greetings.html')
    js_url = url_for('static', filename='add.js')
    return make_response(template.render(name=name,js_url=js_url))     


@app.errorhandler(409)
def payme(e):
    return render_template('error409.html')


# The host='0.0.0.0' means the web app will be accessible to any device on the network
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')