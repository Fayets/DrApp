from pony.orm import *
from src.db import db
from datetime import date

# Modelo Medico
class Medico(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(str, unique=True)
    password = Required(str)
    nombre = Required(str)
    apellido = Required(str)
    dni = Required(str)
    especialidad = Required(str)
    pacientes = Set('Patient')  # Relación uno a muchos con Paciente

    _table_ = "Medicos"

# Modelo Paciente
class Patient(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str)
    apellido = Required(str)
    dni = Required(str, unique=True)
    fecha_nacimiento = Required(date)
    medico = Required(Medico)  # Relación muchos a uno con Medico
    obrasocial = Required(str)
    historia_clinica = Set('HistoriaClinica')  

    _table_ = "Pacientes"

# Modelo HistoriaClinica
class HistoriaClinica(db.Entity):
    id = PrimaryKey(int, auto=True)
    paciente = Required(Patient)  
    fecha_creacion = Required(date)
    alergias = Required(str)  
    condiciones = Required(str)  
    observaciones = Required(str)  
    prescripciones = Required(str)  
    
    _table_ = "HistoriasClinicas"
