#!/bin/bash

function dependencias(){
    pip3 install -r ../requiremenets.txt
}
function entorno(){
    export FLASK_ENV="development"
    export FLASK_APP="programa:servidor_flask"
}
function crearBaseDatos(){
    entorno
    flask db init
}
function estructuraBaseDatos(){
    entorno
    flask db migrate -m 'version1' # Pedir a migrate que nos genere una version de la BBDD con un mensaje de confirmacion
    flask db update    
}
function iniciar(){
    entorno
    flask run
}