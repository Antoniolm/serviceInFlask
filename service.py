from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
import MySQLdb
import json
import os

app = Flask(__name__)

db = MySQLdb.connect(host="localhost",
                       user = "root",
                       passwd = "root",
                       db = "")

# Primero comprobamos si la base de datos esta creada
cursor = db.cursor()
cursor.execute("SELECT count(SCHEMA_NAME) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'pharmaciesDB'")
data = cursor.fetchone()

# Si no lo esta
if data[0]==0:
    os.system("mysql -u root -proot < dbSchema.sql ")
else: #Si lo esta
    db.close();
    db = MySQLdb.connect(host="localhost",
                         user = "root",
                         passwd = "root",
                         db = "pharmaciesDB")

@app.route("/")
def root():
    cursor = db.cursor()
    cursor.execute("select count(*) from information_schema.SCHEMATA where schema_name not in ('mysql','information_schema');")
    data = cursor.fetchone()
    print(data[0])
    return "yeah"

@app.route("/login")
def login():
    cursor = db.cursor()
    cursor.execute("SELECT * from users where name='antonio' and password='prueba'")
    data = cursor.fetchone()
    if data is None:
        return jsonify(login="fail")
    else:
        return jsonify(login="success")

@app.route("/registry")
def registry():
    cursor = db.cursor()
    #data = cursor.execute("INSERT INTO users (name,password,client) VALUES("'+name+'","'+password+'","'+client+'")")
    cursor.execute("INSERT INTO users (name,password,client) VALUES('prueba','prueba',0)")
    db.commit()
    return "hola"

@app.route("/rmUser")
def rmUser():
    id=7;
    cursor = db.cursor()
    cursor.execute("DELETE FROM users where id="+id);
    db.commit()
    return "Removed User"

@app.route("/addProduct")
def addProduct():
    db.commit()
    cursor = db.cursor()
    cursor.execute("INSERT INTO catalog (name,quantity,price) VALUES('pruebaProducto',5,65)")
    db.commit()
    return jsonify(login="success")

@app.route("/modifyProduct")
def modifyProduct():
    return jsonify(login="success")

@app.route("/deleteProduct")
def deleteProduct():
    id=7;
    cursor = db.cursor()
    cursor.execute("DELETE FROM catalog where id="+id);
    db.commit()
    return "Removed Product"

@app.route("/doRequest")
def doRequest():
    return jsonify(login="success")

@app.route("/getCatalog")
def getCatalog():
    jsonResult= jsonify()
    cursor = db.cursor()
    rows=cursor.execute("SELECT name,quantity,price FROM catalog")

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cursor.fetchall()]
    return jsonify(result);

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

# sudo docker build -t antoniolm/prueba .
# sudo docker run -p 5000:5000 -t antonio/prueba
# apt-get python-dev mysql-server libmysqlclient-dev
# pip install mysqlclient flask flask-mysqldb
