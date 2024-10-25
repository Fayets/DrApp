from pydantic import BaseModel
from typing import List
from src.models import Medico

class BaseMedico(BaseModel):
    email = str
    password = str
    nombre = str
    apellido = str 
    dni = str
    especialidad = str

#Esquema para crear un nuevo medico 
class MedicoCreate(BaseMedico):
    pass
