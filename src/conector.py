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
    sql = "SELECT id, names, points FROM users WHERE id = %s"
    valores = (id,)
    mycursor.execute(sql,valores)
    datos = mycursor.fetchone()
    print(datos)
    if datos != None:
        usuario = {'id': datos[0], 'nombre': datos[1], 'puntos': datos[2]}
        return usuario
def crear(id, names, points):
    if id == "-1" or id == -1:
        id = None
    sql = """INSERT INTO users (id, names, points) VALUES (%s, %s, %s)"""
    valores = (id,names,points,)

    mycursor.execute(sql, valores)
    mydb.commit()
def borrar(id):
    sql = "DELETE FROM users WHERE id = '%s'"
    valores (id,)
    mycursor.execute(sql,valores)
    mydb.commit()