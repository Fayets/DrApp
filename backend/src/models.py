from pony.orm import *
from src.db import db
from datetime import date

class Medico(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(str, unique=True) 
    password = Required(str) 
    nombre = Required(str) 
    apellido = Required (str)
    dni = Required(str)
    especialidad = Required (str)
    pacientes = Set('Patient')  # Relación de uno a muchos con Paciente

    _table_ = "Medicos"

class Patient(db.Entity):
    nombre = Required(str)
    apellido = Required(str)
    dni = Required(str, unique=True)
    fecha_nacimiento = Required(date)
    medico = Required(Medico)  # Relación de muchos a uno con Medico
    obrasocial = Required(str)
    historias_clinicas = Set('HistoriaClinica')  # Relación de uno a muchos con HistoriaClinica

    _table_ = "Pacientes"


class HistoriaClinica(db.Entity):
    paciente = Required(Patient)  # Relación de muchos a uno con Paciente
    fecha_creacion = Required(date)
    descripcion = Optional(str)  # Ejemplo de campo para la historia clínica

    _table_ = "Historiaslinicas"

