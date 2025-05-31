from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@login.route('/cliente', methods=['POST'])
def llamarServicioSet():
    ci = request.json.get('ci')
   
    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(user, password):
    ciLocal = "4133266"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    try:
        if ciLocal == ci:
            accion = "Success"
        else:
            print("Cliente no existe")
            accion = "Cliente no encontrado"
            codRes = 'ERROR'
            menRes = 'Cliente no existe en db'


    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion
