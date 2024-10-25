from fastapi import FastAPI #importamos la funciones de FastAPI
from src.db import db

app = FastAPI() #creamos una instancia. Este será el punto de interacción principal para crear todo tu API.


# Mapeando las entidades a tablas (si no existe la tabla, la crea)
db.generate_mapping(create_tables=True)