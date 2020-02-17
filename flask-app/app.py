#!/usr/bin/env/python3.6
from flask import Flask, request, redirect, url_for, Markup, make_response 
from flaskext.mysql import MySQL
from jinja2 import Environment, FileSystemLoader
import subprocess
from http import cookies
from random import randint
from products import Products
from flask.templating import render_template


app = Flask(__name__)
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

@app.route('/', methods=['GET', 'POST','PUT'])
def logins():        
    if request.method == "POST" and ("user" in request.form.keys()) and ("password" in request.form.keys()):
        details = request.form
        user = details['user']
        password = details['password']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS User ("
                            "name VARCHAR(100) NOT NULl,"
                            "PRIMARY KEY(name),"
                            "Wallet FLOAT,"
                            "password  VARCHAR(100))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Product ("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "PRIMARY KEY(id),"
                            "name    VARCHAR(100),"
                            "value    FLOAT,"
                            "Description  VARCHAR(100))")
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
        cursor.execute("SELECT * from User WHERE  name = "+ str(user)+" AND password = "+ str(password))
        conn.commit()
        cursor.close()
        data = cursor.fetchall() 
        if data:
            template = env.get_template('home.html')
            resp = make_response(template.render())
            resp.set_cookie('user', user)
            return resp
        else:
            return redirect('/')

    elif request.method == "POST" and request.form['userR'] != "" and request.form['passwordR'] != "":
        details1 = request.form
        user1 = details1['userR']
        password1 = details1['passwordR']
        conn = mysql.get_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS User ("
                            "name VARCHAR(100) NOT NULl,"
                            "PRIMARY KEY(name),"
                            "Wallet FLOAT,"
                            "password  VARCHAR(100))")
        cursor.execute("CREATE TABLE IF NOT EXISTS Product ("
                            "id INT NOT NULL AUTO_INCREMENT,"
                            "PRIMARY KEY(id),"
                            "name    VARCHAR(100),"
                            "value    FLOAT,"
                            "Description  VARCHAR(100))")
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
        cursor.execute("INSERT INTO User(name, Wallet, password)VALUES ("+user1+", 0, "+password1+")")
        idRand = randint(1, 1000)
        cursor.execute("INSERT INTO CuponExtra(idCupon, idUser, valueMoney)VALUES ("+str(idRand)+", "+ str(user1)+", "+str(100.0)+")")
        conn.commit()
        cursor.close()
        template = env.get_template('home.html')
        resp = make_response(template.render())
        resp.set_cookie('user', user1)
        return resp
        
 
    # return "login and register"
    template = env.get_template('includes/logins.html')
    return make_response(template.render())

@app.route('/home' , methods=['GET', 'POST'])
def show_home():
    conn = mysql.connect()
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM MyPhrases")
    # data = cursor.fetchall()
    cursor.close()
    template = env.get_template('home.html')
    return make_response(template.render())

@app.route('/products' , methods=['GET', 'POST'])
def show_products():
    conn = mysql.connect()
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM MyPhrases")
    # data = cursor.fetchall()
    cursor.close()
    return render_template('productos.html',products = Products)

@app.route('/history' , methods=['GET', 'POST'])
def show_history():
    conn = mysql.connect()
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM MyPhrases")
    # data = cursor.fetchall()
    cursor.close()
    template = env.get_template('history.html')
    return make_response(template.render())            


@app.route('/hello/<name>')
def hello(name):
    template = env.get_template('greetings.html')
    js_url = url_for('static', filename='add.js')
    return make_response(template.render(name=name,js_url=js_url))     

@app.route('/bin', methods=['GET', 'POST'])
def binary_file():
    if request.method == "POST":        
        args = ("gcc","static/script.c", "-o","static/binary_file")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()

    args = ("static/binary_file")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    return output

# The host='0.0.0.0' means the web app will be accessible to any device on the network
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')