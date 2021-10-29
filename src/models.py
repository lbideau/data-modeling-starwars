import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(10))
    user_name = Column(String(30), unique=True)
    favoritoUusario_id = Column(Integer,ForeignKey("FavoritoUsuario.id"))
class FavoritoUsuario(Base):
    __tablename__ = 'FavoritoUsuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey("planeta.id"))
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"))
    persona_id = Column(Integer, ForeignKey("personaje.id"))
    usuario = relationship("Usuario", backref="FavoritoUsuario")
   
class Personaje(Base):
    __tablename__= 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(15),nullable=False, unique=True)
    altura = Column(Float, nullable=False)
    genero = Column(String(15), nullable=False)
    favoritoUsuario= relationship("FavoritoUsuario", backref="personaje")
class Planeta(Base):
    __tablename__= "planeta"
    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(15),nullable=False,unique=True)
    periodo_rotacion = Column(Integer,nullable=False)
    favoritoUsuario= relationship("FavoritoUsuario", backref="planeta")

class Vehiculo(Base):
    __tablename__="vehiculo"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(10),nullable=False,unique=True)
    tipo = Column(String(10),nullable=False)
    fabricante = Column(String(10),nullable=False)
    longitud = Column(Integer,nullable=False)
    favoritoUsuario= relationship("FavoritoUsuario", backref="vehiculo")
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')