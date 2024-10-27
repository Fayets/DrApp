from pony.orm import *
from src.db import db
from datetime import datetime

class Medico(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(str, unique=True) 
    password = Required(str) 
    nombre = Required(str) 
    apellido = Required (str)
    dni = Required(str)
    especialidad = Required (str)
    pacientes = Set('Pacientes')  # Relación de uno a muchos con Paciente

    _table_ = "Medicos"



