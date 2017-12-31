from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
import MySQLdb
import json
import os

app = Flask(__name__)

os.system("service mysql start")
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

########################
## Users
#######################

@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        jsonResult= jsonify()
        cursor = db.cursor()
        rows=cursor.execute("SELECT name,password,client FROM users")

        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cursor.fetchall()]
        return jsonify(result);

    if request.method == 'POST':
        if request.json:
            content= request.get_json()
            username = content.get('name')
            password = content.get('password')
            client = int(content.get('client'))
        else :
            username = request.form['name']
            password = request.form['password']
            client = int(request.form['client'])

        cursor = db.cursor()
        data = cursor.execute("INSERT INTO users (name,password,client) VALUES(%s,%s,%s)",(username,password,client))
        db.commit()

        return jsonify(registry="success")

    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/users/<idUser>", methods=['GET', 'POST' , 'DELETE'])
def user(idUser):
    if request.method == 'GET':
        cursor = db.cursor()

        cursor.execute("SELECT * from users where id=%s", idUser)
        data = cursor.fetchone()

        if data is None:
            return jsonify(error="UsernotFound")
        else:
            return jsonify(name=data[1],password=data[2],client=data[3])

    if request.method == 'POST':
        if request.json:
            content= request.get_json()
            username = content.get('name')
            password = content.get('password')
            client = int(content.get('client'))
        else :
            username = request.form['name']
            password = request.form['password']
            client = int(request.form['client'])

        cursor = db.cursor()
        data = cursor.execute("UPDATE users SET name=%s, password=%s, client=%s WHERE id=%s", (username,password,client,idUser))
        db.commit()

        return jsonify(registry="success")

    if request.method == 'DELETE':
        cursor = db.cursor()
        cursor.execute("DELETE FROM users where id=%s", idUser);
        db.commit()

        return jsonify(removeUser="success")
    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/login", methods=['POST'])
def login():
    if request.json:
        content= request.get_json()
        username = content.get('name')
        password = content.get('password')
    else :
        username = request.form['name']
        password = request.form['password']

    cursor = db.cursor()

    cursor.execute("SELECT * from users where name=%s and password=%s",(username,password))
    data = cursor.fetchone()

    if data is None:
        return jsonify(login="fail")
    else:
        return jsonify(login="success")

########################
## Products
########################

@app.route("/products", methods=['GET', 'POST' , 'DELETE'])
def products():
    if request.method == 'GET':
        jsonResult= jsonify()
        cursor = db.cursor()
        rows=cursor.execute("SELECT name,quantity,price FROM catalog")

        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cursor.fetchall()]
        return jsonify(result);

    if request.method == 'POST':
        if request.json:
            content= request.get_json()
            name = content.get('name')
            quantity = int(content.get('quantity'))
            price = int(content.get('price'))
        else :
            name = request.form['name']
            quantity = int(request.form['quantity'])
            price = int(request.form['price'])

        cursor = db.cursor()
        cursor.execute("INSERT INTO catalog (name,quantity,price) VALUES(%s,%s,%s)", (name,quantity,price))
        db.commit()

        return jsonify(addProduct="success")

    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/products/<idProduct>", methods=['GET', 'POST' , 'DELETE'])
def product(idProduct):
    if request.method == 'GET':
        cursor = db.cursor()

        cursor.execute("SELECT * from catalog where id=%s", idProduct)
        data = cursor.fetchone()

        if data is None:
            return jsonify(error="ProductnotFound")
        else:
            return jsonify(name=data[1],quantity=data[2],price=data[3])

    if request.method == 'POST':
        if request.json:
            content= request.get_json()
            name = content.get('name')
            quantity = int(content.get('quantity'))
            price = int(content.get('price'))
        else :
            name = request.form['name']
            quantity = int(request.form['quantity'])
            price = int(request.form['price'])

        cursor = db.cursor()
        data = cursor.execute("UPDATE catalog SET name=%s, quantity=%s, price=%s WHERE id=%s", (name,quantity,price,idProduct))
        db.commit()

        return jsonify(addProduct="success")

    if request.method == 'DELETE':
        cursor = db.cursor()
        cursor.execute("DELETE FROM catalog where id=%s", idProduct);
        db.commit()

        return jsonify(removeProduct="success")
    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/doRequest", methods=['GET', 'POST'])
def doRequest():
    return jsonify(login="success")

########################
## Pharmacies
########################

@app.route("/pharmacies", methods=['GET', 'POST' , 'DELETE'])
def pharmacies():
    if request.method == 'GET':
        jsonResult= jsonify()
        cursor = db.cursor()
        rows=cursor.execute("SELECT name,latitude,longitude FROM pharmacies")

        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cursor.fetchall()]
        return jsonify(result);

    if request.method == 'POST':
        if request.json:
            content= request.get_json()
            name = content.get('name')
            latitude = float(content.get('latitude'))
            longitude = float(content.get('longitude'))
        else :
            name = request.form['name']
            latitude = float(request.form['latitude'])
            longitude = float(request.form['longitude'])

        cursor = db.cursor()
        cursor.execute("INSERT INTO pharmacies (name,latitude,longitude) VALUES(%s,%s,%s)", (name,latitude,longitude))
        db.commit()

        return jsonify(addPharmacies="success")

    return jsonify(error="DontMethodDetected")

###################################################################

@app.route("/pharmacies/<idPharma>", methods=['GET', 'POST' , 'DELETE'])
def pharmacy(idPharma):
    if request.method == 'GET':
        cursor = db.cursor()

        cursor.execute("SELECT * from pharmacies where id=%s", idPharma)
        data = cursor.fetchone()

        if data is None:
            return jsonify(error="PharmacynotFound")
        else:
            return jsonify(name=data[1],latitude=data[2],longitude=data[3])

    if request.method == 'POST':
        if request.json:
            content= request.get_json()
            name = content.get('name')
            latitude = float(content.get('latitude'))
            longitude = float(content.get('longitude'))
        else :
            name = request.form['name']
            latitude = float(request.form['latitude'])
            longitude = float(request.form['longitude'])

        cursor = db.cursor()
        data = cursor.execute("UPDATE pharmacies SET name=%s, latitude=%s, longitude=%s WHERE id=%s", (name,latitude,longitude,idPharma))
        db.commit()

        return jsonify(updatePharmacy="success")

    if request.method == 'DELETE':
        cursor = db.cursor()
        cursor.execute("DELETE FROM pharmacies where id=%s", idPharma);
        db.commit()

        return jsonify(removePharmacy="success")
    return jsonify(error="DontMethodDetected")

###################################################################
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#curl -X POST localhost:5000/users/0 -d nm=post2 -d pass=sip -d client=0
#curl -X DELETE localhost:5000/users/6
#curl localhost:5000/users/2

# sudo docker build -t antoniolm/prueba .
# sudo docker run -p 5000:5000 -t antonio/prueba
# apt-get python-dev mysql-server libmysqlclient-dev
# pip install mysqlclient flask flask-mysqldb
