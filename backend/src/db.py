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


