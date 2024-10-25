from pony.orm import *
from src.db import db

class Medico(db.Entity):
    id = PrimaryKey(auto=True)
    email = Required(str, unique=True) 
    password = Required(str) 
    nombre = Required(str) 
    apellido = Required (str)
    dni = Required(str)
    especialidad = Required (str)
    _table_ = "Medicos"
