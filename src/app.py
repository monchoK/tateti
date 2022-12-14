
from flask import Flask, jsonify, request
from validar import *
import conector
from config import config


app=Flask(__name__)




@app.route("/", methods=["GET"])
def get_usuarios():
        try:
                usuarios = conector.leer()
                return jsonify({"mensaje":"lista de usuarios","usuarios":usuarios})
         
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
    
@app.route('/usuarios/<id>', methods=['GET'])
def leer_usuario(id):
    try:
        usuario = conector.leer_usuario(id)
        if usuario != None:
            return jsonify({'usuario': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False, 'usuario': usuario})


@app.route('/usuarios', methods=['POST'])
def post_usuarios():
    
    if (validar_names(request.json['names']) ):
        try:
            usuario = conector.leer_usuario_nombre(request.json['names'])
            if usuario != None:
                return jsonify({'mensaje': "Usuario ya existe con este nombre.", 'exito': False})
            else:
                conector.crear(request.json['names'])
                return jsonify({'mensaje': "usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuarios(id):
    try:
        usuario = conector.leer_usuario(id)
        if usuario != None:
            conector.borrar(id)
            return jsonify({'mensaje': "Usuario eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

 #OPCIONES DE DESARROLLADOR PARA FLASK ESTA EN CONFIG DEVELOPMENTCONFIG
if __name__ == "__main__":
    app.config.from_object(config["development"])

    app.run()