from pony.orm import *
from decouple import config

db = Database()

#Binding, establecer la conexion con la base de datos.

db.bind(
    provider='postgres',
    user='mydb_owner',
    password='Pl62CeNFQXIM',
    host='ep-white-hill-a5ocdvcq.us-east-2.aws.neon.tech',
    database='mydb',
    port=5432,
    sslmode='require'  # Asegura que se use SSL, Neon lo requiere
)

# Definir una sesión para probar la conexión
"""@db_session
def prueba_conexion():
    try:
        # Intenta obtener alguna información de la base de datos
        db.execute("SELECT 1")
        print("Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"Error en la conexión: {e}")"""

