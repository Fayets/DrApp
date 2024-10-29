from pony.orm import *
from src.db import db
from datetime import date

# Define el modelo Medico
class Medico(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(str, unique=True) 
    password = Required(str) 
    nombre = Required(str) 
    apellido = Required(str)
    dni = Required(str)
    especialidad = Required(str)
    pacientes = Set('Patient')  # Relación de uno a muchos con Paciente

    _table_ = "Medicos"

# Define el modelo Patient
class Patient(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str)
    apellido = Required(str)
    dni = Required(str, unique=True)
    fecha_nacimiento = Required(date)
    medico = Required(Medico)  # Relación de muchos a uno con Medico
    obrasocial = Required(str)
    historias_clinicas = Set('HistoriaClinica')  # Relación de uno a muchos con HistoriaClinica

    _table_ = "Pacientes"

# Define el modelo HistoriaClinica
class HistoriaClinica(db.Entity):
    id = PrimaryKey(int, auto=True)
    paciente = Required(Patient)  # Relación de muchos a uno con Paciente
    fecha_creacion = Required(date, default=lambda: date.today())
    descripcion = Optional(str)

    _table_ = "HistoriasClinicas"
