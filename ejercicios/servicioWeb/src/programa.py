from config import test
from flask import Flask
from servicios import configurarServicios

configuracion = test # TODO: Cargar la conf desde una variable e entorno

servidor_flask=Flask(__name__) # Creamos un servidor de flask, con el mismo nombre que el modulo
servidor_flask.config.from_object(configuracion) # Establecer configuración basica del servidor:
                                                 # Puerto...
                                                 # tipo de entorno: Desarrollo, produccion
configurarServicios(servidor_flask)              # Alta de los servicios en el servidor de flask
#servidor_flask.run()