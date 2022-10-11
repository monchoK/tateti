#Clase configuraciones de desarrollador, devuelve  un diccionario que tiene la instancia de las clases
class DevelopmentConfig():
    DEBUG=True 
    MYSQL_HOST ="127.0.0.1"
    MYSQL_USER ="root"
    MYSQL_PASSWORD ="secret"
    MYSQL_DB="Tateti"

config = {"development":DevelopmentConfig}

