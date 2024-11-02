from pony.orm import db_session
from pony.orm.core import TransactionIntegrityError
from src import models, schemas
from pydantic import BaseModel, EmailStr
from fastapi import HTTPException

class MedicoService:

    def __init__(self):
        pass
    
    def create_medico(self, medico: schemas.MedicoCreate):
        with db_session:
            try:
                nuevo_medico = models.Medico(
                    email=medico.email,
                    password=medico.password,
                    nombre=medico.nombre,
                    apellido=medico.apellido,
                    dni=medico.dni,
                    especialidad=medico.especialidad
                )
                print("Medico creado correctamente")
                return nuevo_medico  
            except TransactionIntegrityError as e:
                print(f"Error de integridad transaccional: {e}")
                raise HTTPException(status_code=400, detail=str(e))  
            except Exception as e:
                print(f"Error al crear el usuario: {e}")
                raise HTTPException(status_code=500, detail="Error inesperado")

                
    @staticmethod
    @db_session
    def authenticate_medico(email: str, password: str):
        medico = models.Medico.get(email=email)
        if medico and medico.password == password:
            return medico
        return None



