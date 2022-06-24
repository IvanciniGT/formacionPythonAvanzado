from flask_sqlalchemy import SQLAlchemy
base_datos = SQLAlchemy() # Falta info de conexión

from flask_marshmallow import Marshmallow
serializador_json = Marshmallow() 

from flask_migrate import Migrate
gestor_estructura_base_datos = Migrate()

# todos_los_apis_que_ofrezca_este_modulo
from flask import Blueprint
mi_blueprint = Blueprint('api_servicios', __name__ )
