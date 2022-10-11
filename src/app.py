
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from validaciones import *

from config import config

app=Flask(__name__)

conexion=MySQL(app)


@app.route("/", methods=["GET"])
def get_tateti():
        try:
                cursor = conexion.connection.cursor()
                cursor.execute("""SELECT * FROM users""")
                data = cursor.fetchall()

                usuarios=[]
                for fila in data:
                        usuario ={"id":fila[0],"nombre":fila[1],"puntos":fila[2]}
                        usuarios.append(usuario)
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
        usuario = leer_usuario_bd(id)
        if usuario != None:
            return jsonify({'usuario': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Uusuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    # print(request.json)
    if (validar_id(request.json['id']) and validar_names(request.json['names']) and validar_points(request.json['points'])):
        try:
            usuario = leer_usuario_bd(request.json['id'])
            if usuario != None:
                return jsonify({'mensaje': "Usuario ya existe, no se puede duplicar.", 'exito': False})
            else:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO users (id, names, points) 
                VALUES ('{0}', '{1}', {2})""".format(request.json['id'],
                                                     request.json['names'], request.json['points'])
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de inserción.
                return jsonify({'mensaje': "usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


if __name__ == "__main__":
    app.config.from_object(config["development"]) #OPCIONES DE DESARROLLADOR PARA FLASK ESTA EN CONFIG DEVELOPMENTCONFIG

    app.run()