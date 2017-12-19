from flask import Flask
from flask import jsonify
from flask import render_template
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

conn = MySQLdb.connect(host="localhost",
                       user = "root",
                       passwd = "root",
                       db = "farmacias")
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
    return jsonify(login="success")

@app.route("/rmUser")
def rmUser():
    return jsonify(login="success")

@app.route("/addProduct")
def addProduct():
    return jsonify(login="success")

@app.route("/modifyProduct")
def modifyProduct():
    return jsonify(login="success")

@app.route("/deleteProduct")
def deleteProduct():
    return jsonify(login="success")

@app.route("/getCatalog")
def getCatalog():
    return jsonify(login="success")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')



# apt-get python-dev mysql_server libmysqlclient-dev
# pip install mysqlclient flask flask-mysqldb
#
# CREATE TABLE users ( id INT NULL AUTO_INCREMENT, name VARCHAR(45) NULL,
# password VARCHAR(45) NULL, PRIMARY KEY (id));
