
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from validar import *
import conector
from config import config

app=Flask(__name__)

conexion=MySQL(app)


@app.route("/", methods=["GET"])
def get_usuarios():
        try:
                usuarios = conector.leer()
                return jsonify({"mensaje":"lista de usuarios","usuarios":usuarios})
         
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})

def leer_usuario_bd(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, names, points FROM users WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'id': datos[0], 'nombre': datos[1], 'puntos': datos[2]}
            return usuario
        else:
            return None
    except Exception as ex:
        raise ex                
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
    
    if (validar_id(request.json['id']) and validar_names(request.json['names']) and validar_points(request.json['points'])):
        try:
            usuario = leer_usuario_bd(request.json['id'])
            if usuario != None:
                return jsonify({'mensaje': "Usuario ya existe, no se puede duplicar.", 'exito': False})
            else:
                conector.crear(request.json['id'], request.json['names'], request.json['points'])
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
            # conector.borrar(id)
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM users WHERE id = '{0}'".format(id)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Usuario eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


if __name__ == "__main__":
    app.config.from_object(config["development"]) #OPCIONES DE DESARROLLADOR PARA FLASK ESTA EN CONFIG DEVELOPMENTCONFIG

    app.run()