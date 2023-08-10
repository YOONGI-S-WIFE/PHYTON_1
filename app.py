from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

#creacion y configuracion de la app

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3307/flask-shopy-2687365'

#crear objetos de SQLAlchemy y migrate

db = SQLAlchemy(app)
migrate = Migrate(app , db)

#modelos

class Cliente(db.Model):
    id = db.Column( db.Integer, primary_key = True)
    user = db.Column( db.String(100) , unique = True)
    email = db.Column( db.String(200) , unique = True)
    password =db.Column( db.String(200))
  
class Producto(db.Model):
    id = db.Column( db.Integer , primary_key = True)
    nombre = db.Column( db.String(100) )
    precio = db.Column( db.Numeric (precision = 10, scale = 2))
    imagen =db.Column( db.String(200))

class Venta(db.Model):
    id = db.Column( db.Integer, primary_key = True)
    fecha = db.Column( db.DateTime, default = datetime.utcnow)
    id_cliente = db.Column (db.Integer, db.ForeignKey ('cliente.id'))

class Detalle(db.Model):
    id = db.Column( db.Integer, primary_key = True)
    cantidad = db.Column ( db.Integer)
    id_productofk = db.Column (db.Integer, db.ForeignKey ('producto.id'))
    id_ventafk = db.Column (db.Integer, db.ForeignKey ('venta.id'))

