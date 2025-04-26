#!/usr/bin/env python3
from flask import Flask
from login import login
from login2 import login2

app = Flask(__name__)

# Registrar el blueprint de login
app.register_blueprint(login)

app.register_blueprint(login2)
@app.route('/', methods=['GET'])
def hello():
    return 'Hola Unida'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
