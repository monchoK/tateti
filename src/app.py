
from flask import Flask, jsonify
from flask_mysqldb import MySQL

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

if __name__ == "__main__":
    app.config.from_object(config["development"]) #OPCIONES DE DESARROLLADOR PARA FLASK ESTA EN CONFIG DEVELOPMENTCONFIG

    app.run()