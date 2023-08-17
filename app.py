from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_bootstrap import Bootstrap

#creacion y configuracion de la app

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3306/flask-shopy-2687365'
app.config["SECRET_KEY"] = "!puto_el_que_lo_lea¡"
b = Bootstrap(app)

#crear objetos de SQLAlchemy y migrate

db = SQLAlchemy(app)
migrate = Migrate(app , db)

#modelos

class Cliente(db.Model):
    
    __tablename__ = "cliente"
    
    id = db.Column( db.Integer, primary_key = True)
    user = db.Column( db.String(100) , unique = True)
    email = db.Column( db.String(200) , unique = True)
    password =db.Column( db.String(200))
  
class Producto(db.Model):
    
    __tablename__ = "producto"

    id = db.Column( db.Integer , primary_key = True)
    nombre = db.Column( db.String(100) )
    precio = db.Column( db.Numeric (precision = 10, scale = 2))
    imagen =db.Column( db.String(200))

class Venta(db.Model):
    
    __tablename__ = "venta"

    id = db.Column( db.Integer, primary_key = True)
    fecha = db.Column( db.DateTime, default = datetime.utcnow)
    id_cliente = db.Column (db.Integer, db.ForeignKey ('cliente.id'))

class Detalle(db.Model):
    
    __tablename__ = "detalle"

    id = db.Column( db.Integer, primary_key = True)
    cantidad = db.Column ( db.Integer)
    id_productofk = db.Column (db.Integer, db.ForeignKey ('producto.id'))
    id_ventafk = db.Column (db.Integer, db.ForeignKey ('venta.id'))
    
    #definir el formulario
    #de registro de producto
    
class NuevoProductoForm(FlaskForm):
    nombre = StringField("Nombre del producto")
    precio = StringField("Precio del preducto")
    submit = SubmitField("Registrar")

@app.route("/registrar_producto", methods=['GET', 'POST'])
def registrar():
    form = NuevoProductoForm()
    p = Producto()
    if form.validate_on_submit():
        #registrar el producto en db
        #p = Producto(nombre = form.nombre.data,
        #            precio = form.precio.data)
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return "producto registrado"
    return render_template("registrar.html", form = form)