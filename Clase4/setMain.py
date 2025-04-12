#!/usr/bin/env python
# -*- Coding: utf-8 -*-
# Línea shebang: permite ejecutar este script directamente en sistemas Unix/Linux
# Codificación UTF-8 para permitir caracteres especiales

from flask import Flask, jsonify, request
# Importamos Flask para crear la app web, jsonify para devolver respuestas en JSON
# y request para manejar datos entrantes (por ejemplo, de formularios o JSON)


app = Flask(__name__) 
# Creamos la instancia de la aplicación Flask


@app.route('/', methods=['GET'])
def hello():
    # Definimos una ruta para el endpoint raíz "/" que responde a solicitudes GET
    return 'Hola  Unida!'
    # Al acceder a la raíz del sitio, se devuelve este mensaje
@app.route('/hola', methods=['GET'])
def hola():
    # Definimos una ruta para el endpoint raíz "/" que responde a solicitudes GET
    return 'Hola 2  Unida!'
    # Al acceder a la raíz del sitio, se devuelve este mensaje
@app.route('/unida', methods=['GET'])
def unida():
    # Definimos una ruta para el endpoint raíz "/" que responde a solicitudes GET
    return 'Unida!'
    # Al acceder a la raíz del sitio, se devuelve este mensaje
     
if __name__ == "__main__":
    # Este bloque se ejecuta solo si el script se ejecuta directamente (no importado como módulo)

    ## app.run(host = '127.0.0.1', debug = True, port = 5000)
    # Línea comentada: ejecutaría el servidor localmente solo accesible desde la misma máquina

    app.run(host = '0.0.0.0', debug = True, port = 5000)
    # Ejecuta la app en el host 0.0.0.0, lo cual la hace accesible desde otras máquinas en la red
    # El modo debug permite ver errores detallados y reinicia el servidor al detectar cambios

    app.run(debug = True)
    # Esta línea está de más, ya que `app.run` ya fue llamada antes.
    # En la práctica, solo una llamada a `app.run()` es necesaria.
