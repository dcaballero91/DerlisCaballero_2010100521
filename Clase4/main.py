#!/usr/bin/env python3
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from login import login

app = Flask(__name__)

# Registrar el blueprint de login
app.register_blueprint(login)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Mundo'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
