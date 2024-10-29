from pydantic import BaseModel, EmailStr
from typing import List, Optional
from src.models import Medico
from datetime import date

class BaseMedico(BaseModel):
    email: EmailStr
    password: str
    nombre: str
    apellido: str 
    dni: str
    especialidad: str

#Esquema para crear un nuevo medico 
class MedicoCreate(BaseMedico):
    pass

#Esquema para el login 
class LoginData(BaseModel):
    email: EmailStr
    password: str

#-----------------------------------------#


class RegisterMessage(BaseModel):
    message: str
    success: bool

#-----------------------------------------#

# Esquema para una historia clínica
class HistoriaClinicaCreate(BaseModel):
    descripcion: Optional[str] = None

#-----------------------------------------#


# Esquema para creación de paciente
class PatientCreate(BaseModel):
    nombre: str
    apellido: str
    dni: str
    fecha_nacimiento: date
    obrasocial: str
    medico_id: int

class PatientUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    dni: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    obrasocial: Optional[str] = None

# Esquema de respuesta para ver paciente y sus historias clínicas
class PacienteResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    dni: str
    fecha_nacimiento: date
    obrasocial: str
    medico_id: int  








