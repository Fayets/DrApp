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

# Modelo Paciente (Patient)
class Patient(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str)
    apellido = Required(str)
    dni = Required(str, unique=True)
    fecha_nacimiento = Required(date)
    medico = Required(Medico)  # Relación muchos a uno con Medico
    obrasocial = Required(str)
    historia_clinica = Optional('HistoriaClinica')  # Relación uno a uno con HistoriaClinica

    _table_ = "Pacientes"

# Modelo HistoriaClinica (Contenedor principal de toda la información clínica del paciente)
class HistoriaClinica(db.Entity):
    id = PrimaryKey(int, auto=True)
    paciente = Required(Patient)  # Relación uno a uno con Paciente
    fecha_creacion = Required(date, default=lambda: date.today())
    alergias = Set('Alergia')  # Relación uno a muchos con Alergias
    condiciones = Set('Condicion')  # Relación uno a muchos con Condiciones
    observaciones = Set('Observacion')  # Relación uno a muchos con Observaciones
    medicamentos = Set('MedicationRequest')  # Relación uno a muchos con MedicationRequest

    _table_ = "HistoriasClinicas"

# Modelo Alergia
class Alergia(db.Entity):
    id = PrimaryKey(int, auto=True)
    historia_clinica = Required(HistoriaClinica)  # Relación muchos a uno con HistoriaClinica
    sustancia = Required(str)
    reaccion = Required(str)
    estado_clinico = Required(str)
    gravedad = Required(str)

    _table_ = "Alergias"

# Modelo Condicion (Enfermedades/Condiciones)
class Condicion(db.Entity):
    id = PrimaryKey(int, auto=True)
    historia_clinica = Required(HistoriaClinica)  # Relación muchos a uno con HistoriaClinica
    diagnostico = Required(str)
    gravedad = Required(str)
    fecha_inicio = Required(date)
    fecha_fin = Optional(date)
    notas_clinicas = Optional(str)

    _table_ = "Condiciones"

# Modelo Observacion (Signos vitales, resultados de laboratorio)
class Observacion(db.Entity):
    id = PrimaryKey(int, auto=True)
    historia_clinica = Required(HistoriaClinica)  # Relación muchos a uno con HistoriaClinica
    tipo = Required(str)  # Tipo de observación, como "Signos vitales", "Laboratorio"
    descripcion = Required(str)
    fecha = Required(date)

    _table_ = "Observaciones"

# Modelo MedicationRequest (Prescripciones Médicas)
class MedicationRequest(db.Entity):
    id = PrimaryKey(int, auto=True)
    historia_clinica = Required(HistoriaClinica)  # Relación muchos a uno con HistoriaClinica
    medicamento = Required(str)  # Nombre del fármaco
    dosis = Required(str)  # Cantidad y frecuencia
    duracion = Required(str)  # Tiempo de uso
    indicaciones = Required(str)  # Cómo y cuándo tomar
    estado_receta = Required(str)  # Activa, completada, suspendida

    _table_ = "PrescripcionesMedicas"
