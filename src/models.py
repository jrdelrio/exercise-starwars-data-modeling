import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    url = Column(String, unique=True)
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer)
    surface_water = Column(Integer)
    url = Column(String)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    charac_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
 
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    starship_class = Column(String)
    manufacturer = Column(String)
    url = Column(Integer)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
