from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class BaseMedico(BaseModel):
    email: EmailStr
    password: str
    nombre: str
    apellido: str 
    dni: str
    especialidad: str

# Esquema para crear un nuevo médico 
class MedicoCreate(BaseMedico):
    pass

# Esquema para el login 
class LoginData(BaseModel):
    email: EmailStr
    password: str
#-----------------------------------------#

class RegisterMessage(BaseModel):
    message: str
    success: bool

#-----------------------------------------#

# Esquema para crear una historia clínica
class HistoriaClinicaCreate(BaseModel):
    #paciente_id: int  
    fecha_creacion: date  
    alergias: str  
    condiciones: str  
    observaciones: str  
    prescripciones: str 

# Esquema para actualizar una historia clínica
class HistoriaClinicaUpdate(BaseModel):
    alergias: Optional[str] = None  # Campos opcionales para la actualización
    condiciones: Optional[str] = None 
    observaciones: Optional[str] = None 
    prescripciones: Optional[str] = None 

#-----------------------------------------#

# Esquema para la creación de paciente
class PatientCreate(BaseModel):
    nombre: str
    apellido: str
    dni: str
    fecha_nacimiento: date
    obrasocial: str
    medico_id: int  # ID del médico asignado

class PatientUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    obrasocial: Optional[str] = None

#-----------------------------------------#

# Esquema de respuesta para la historia clínica
class HistoriaClinicaResponse(BaseModel):
    id: int
    fecha_creacion: date
    alergias: str
    condiciones: str
    observaciones: str
    prescripciones: str

# Esquema de respuesta para ver paciente y sus historias clínicas
class PacienteResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    fecha_nacimiento: date
    obrasocial: str
    medico_id: int  # Este campo debe estar presente
    historias_clinicas: List[HistoriaClinicaResponse] = []
