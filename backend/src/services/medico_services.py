from pony.orm import db_session
from pony.orm.core import TransactionIntegrityError
from src import models, schemas
from pydantic import BaseModel, EmailStr

class MedicoService:

    def __init__(self):
        pass
    
    def create_medico(medico: schemas.MedicoCreate):
        with db_session:
            try:
                medico = models.Medico(
                    email=medico.email,
                    password=medico.password,
                    nombre=medico.nombre,
                    apellido=medico.apellido,
                    dni=medico.dni,
                    especialidad=medico.especialidad
                )
                print("Medico creado correctamente")
                medico_dict = medico.to_dict(exclude=['id'])
                return medico_dict
            except TransactionIntegrityError as e:
                print(f"Error de integridad transaccional: {e}")
            except Exception as e:
                print(f"Error al crear el usuario: {e}")
                
    @staticmethod
    @db_session
    def authenticate_medico(email: str, password: str):
        medico = models.Medico.get(email=email)
        if medico and medico.password == password:
            return medico
        return None



