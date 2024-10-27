from pydantic import BaseModel, EmailStr
from typing import List
from src.models import Medico

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

class RegisterMessage(BaseModel):
    message: str
    success: bool



