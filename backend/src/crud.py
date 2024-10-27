from . import models, schemas
from pony.orm import *
from fastapi import HTTPException

def create_medico(medico: schemas.MedicoCreate):
    with db_session:
        try:
            medico = models.Medico(email=medico.email,password=medico.password, nombre=medico.nombre, apellido=medico.apellido,
                                   dni=medico.dni,especialidad=medico.especialidad)
            print("Medico creado correctamente")
            medico_dict = medico.to_dict(exclude=['id'])
            return medico_dict
        except TransactionIntegrityError as e:
            print(f"Error de integridad transaccional: {e}")
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
