CREATE DATABASE pharmaciesDB;
use pharmaciesDB;

CREATE TABLE users ( id INT NULL AUTO_INCREMENT,
                     name VARCHAR(45) NULL,
                     password VARCHAR(45) NULL,
                     client tinyint(1) ,PRIMARY KEY (id));

INSERT INTO users (name,password,client) VALUES('antonio','prueba',1);
INSERT INTO users (name,password,client) VALUES('farmaceutico','pruebafar',0);


CREATE TABLE catalog ( id INT NULL AUTO_INCREMENT,
                       name VARCHAR(45) NULL,
                       quantity INT NULL,
                       price INT NULL,
                       PRIMARY KEY (id));

INSERT INTO catalog (name,quantity,price) VALUES('gelocatil',5,10);
INSERT INTO catalog (name,quantity,price) VALUES('aspirina',50,2);
INSERT INTO catalog (name,quantity,price) VALUES('vendas',25,3);
INSERT INTO catalog (name,quantity,price) VALUES('baston',3,20);

CREATE TABLE pharmacies ( id INT NULL AUTO_INCREMENT,
                       name VARCHAR(45) NULL,
                       latitude FLOAT NULL,
                       longitude FLOAT NULL,
                       PRIMARY KEY (id));

INSERT INTO pharmacies (name,latitude,longitude) VALUES('Pharmacy 1',37.193837, -3.620339);
INSERT INTO pharmacies (name,latitude,longitude) VALUES('Pharmacy 2',37.198297, -3.620067);
INSERT INTO pharmacies (name,latitude,longitude) VALUES('Pharmacy 3',37.195152, -3.611430);
INSERT INTO pharmacies (name,latitude,longitude) VALUES('Pharmacy 4',37.188775, -3.614289);
INSERT INTO pharmacies (name,latitude,longitude) VALUES('Pharmacy 5',37.186811, -3.603343);
