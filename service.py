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

@app.route("/users/<idUser>", methods=['GET', 'POST' , 'DELETE'])
def users(idUser):
    if request.method == 'GET':
        #idUser = request.args.get('id')
        cursor = db.cursor()

        cursor.execute("SELECT * from users where id=%s", idUser)
        data = cursor.fetchone()

        if data is None:
            return jsonify(users="notFound")
        else:
            return jsonify(name=data[1],password=data[2])

    if request.method == 'POST':
        username = request.form['nm']
        password = request.form['pass']
        client = int(request.form['client'])

        cursor = db.cursor()
        data = cursor.execute("INSERT INTO users (name,password,client) VALUES(%s,%s,%s)",(username,password,client))
        db.commit()

        return jsonify(registry="success")

    if request.method == 'DELETE':
        #idU= request.args.get('id')

        cursor = db.cursor()
        cursor.execute("DELETE FROM users where id=%s", idUser);
        db.commit()

        return jsonify(removeUser="success")
    return jsonify(error="DontMethodDetected")

@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.args.get('nm')
    password = request.args.get('pass')
    cursor = db.cursor()

    cursor.execute("SELECT * from users where name=%s and password=%s",(username,password))
    data = cursor.fetchone()

    if data is None:
        return jsonify(login="fail")
    else:
        return jsonify(login="success")

@app.route("/addProduct", methods=['GET', 'POST'])
def addProduct():
    name = request.args.get('nm')
    quantity = int(request.args.get('quantity'))
    price = int(request.args.get('price'))

    cursor = db.cursor()
    cursor.execute("INSERT INTO catalog (name,quantity,price) VALUES(%s,%s,%s)", (name,quantity,price))
    db.commit()

    return jsonify(login="success")

@app.route("/modifyProduct", methods=['GET', 'POST'])
def modifyProduct():
    return jsonify(login="success")

@app.route("/deleteProduct", methods=['GET', 'POST'])
def deleteProduct():
    id= request.args.get('id')

    cursor = db.cursor()
    cursor.execute("DELETE FROM catalog where id=%s", id);
    db.commit()

    return "Removed Product"

@app.route("/doRequest", methods=['GET', 'POST'])
def doRequest():
    return jsonify(login="success")

@app.route("/getCatalog", methods=['GET', 'POST'])
def getCatalog():
    jsonResult= jsonify()
    cursor = db.cursor()
    rows=cursor.execute("SELECT name,quantity,price FROM catalog")

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cursor.fetchall()]
    return jsonify(result);

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#curl -X POST localhost:5000/users/0 -d nm=post2 -d pass=sip -d client=0
#curl -X DELETE localhost:5000/users/6
#curl localhost:5000/users/2

# sudo docker build -t antoniolm/prueba .
# sudo docker run -p 5000:5000 -t antonio/prueba
# apt-get python-dev mysql-server libmysqlclient-dev
# pip install mysqlclient flask flask-mysqldb
