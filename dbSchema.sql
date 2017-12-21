CREATE DATABASE pharmaciesDB;
use pharmaciesDB;

CREATE TABLE users ( id INT NULL AUTO_INCREMENT,
                     name VARCHAR(45) NULL,
                     password VARCHAR(45) NULL,
                     client tinyint(1) ,PRIMARY KEY (id));

CREATE TABLE catalog ( id INT NULL AUTO_INCREMENT,
                       name VARCHAR(45) NULL,
                       quantity INT NULL,
                       price INT NULL,
                       PRIMARY KEY (id));


INSERT INTO users (name,password,client) VALUES('antonio','prueba',1);
INSERT INTO users (name,password,client) VALUES('farmaceutico','pruebafar',0);

INSERT INTO catalog (name,quantity,price) VALUES('gelocatil',5,10);
INSERT INTO catalog (name,quantity,price) VALUES('aspirina',50,2);
INSERT INTO catalog (name,quantity,price) VALUES('vendas',25,3);
INSERT INTO catalog (name,quantity,price) VALUES('baston',3,20);
