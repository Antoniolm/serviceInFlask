from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

conn = MySQLdb.connect(host="localhost",
                       user = "root",
                       passwd = "root",
                       db = "pharmaciesDB")
cursor = conn.cursor()

@app.route("/")
def root():
    return jsonify(login="success")

@app.route("/login")
def login():
    cursor = conn.cursor()
    cursor.execute("SELECT * from users where name='antonio' and password='prueba'")
    data = cursor.fetchone()
    if data is None:
        return jsonify(login="fail")
    else:
        return jsonify(login="success")

@app.route("/registry")
def registry():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name,password,client) VALUES("'+name+'","'+password+'","'+client+'")")
    data = cursor.fetchone()
    if data is None:
        return jsonify(registry="fail")
    else:
        return jsonify(registry="success")

@app.route("/rmUser")
def rmUser():
    id=1;
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users where id="+id);
    data = cursor.fetchone()
    if data is None:
        return jsonify(removeUser="fail")
    else:
        return jsonify(removeUser="success")

@app.route("/addProduct")
def addProduct():
    return jsonify(login="success")

@app.route("/modifyProduct")
def modifyProduct():
    return jsonify(login="success")

@app.route("/deleteProduct")
def deleteProduct():
    return jsonify(login="success")

@app.route("/doRequest")
def doRequest():
    return jsonify(login="success")

@app.route("/getCatalog")
def getCatalog():
    return jsonify(login="success")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


# apt-get python-dev mysql_server libmysqlclient-dev
# pip install mysqlclient flask flask-mysqldb
#
# CREATE DATABASE pharmaciesDB
#
# CREATE TABLE users ( id INT NULL AUTO_INCREMENT, name VARCHAR(45) NULL,
# password VARCHAR(45) NULL, client tinyint(1) ,PRIMARY KEY (id));
#
# CREATE TABLE catalog ( id INT NULL AUTO_INCREMENT, name VARCHAR(45) NULL,
# quantity INT NULL, price INT NULL, PRIMARY KEY (id));
