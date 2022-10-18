import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="secret",
  database="Tateti"
)

mycursor = mydb.cursor()
def leer():
    mycursor.execute("SELECT * FROM users")
    data = mycursor.fetchall()
    usuarios=[]
    for fila in data:
        usuario ={"id":fila[0],"nombre":fila[1],"puntos":fila[2]}
        usuarios.append(usuario)
    return usuarios
def leer_usuario(id):
    sql = "SELECT id, names, points FROM users WHERE id = %s  "
    valores = (id,)
    mycursor.execute(sql,valores)
    datos = mycursor.fetchone()
    print(datos)
    if datos != None:
        usuario = {'id': datos[0], 'nombre': datos[1], 'puntos': datos[2]}
        return usuario
def leer_usuario_nombre(names):
    sql = "SELECT id, names, points FROM users WHERE names = %s  "
    valores = (names,)
    mycursor.execute(sql,valores)
    datos = mycursor.fetchone()
    print(datos)
    if datos != None:
        usuario = {'id': datos[0], 'nombre': datos[1], 'puntos': datos[2]}
        return usuario

def crear(names):
    
    sql = """INSERT INTO users (names, points) VALUES ( %s, 0)"""
    valores = (names,)

    mycursor.execute(sql, valores)
    mydb.commit()
def borrar(id):
    sql = "DELETE FROM users WHERE id = %s"
    valores =(id,)
    mycursor.execute(sql,valores)
    mydb.commit()