# Configuración de flask
import os

SECRET_KEY = os.urandom(12)

# Configuración de SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///pokemons.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False