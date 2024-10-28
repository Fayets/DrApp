from pony.orm import db_session
from pony.orm.core import TransactionIntegrityError
from src import models, schemas
from src.schemas import PatientCreate
from pydantic import BaseModel
from fastapi import HTTPException
from pony.orm import db_session, select
from src import models, schemas

class PatientService:

    @db_session
    def create_patient(self, patient_data: schemas.PatientCreate):
        try:
            # Verifica si el médico existe
            medico = models.Medico.get(id=patient_data.medico_id)  # Uso correcto de patient_data
            if not medico:
                raise HTTPException(status_code=404, detail="Médico no encontrado")
            
            # Lógica para crear un paciente
            patient = models.Patient(
                nombre=patient_data.nombre,  # Uso correcto de patient_data
                apellido=patient_data.apellido,  # Uso correcto de patient_data
                dni=patient_data.dni,  # Uso correcto de patient_data
                fecha_nacimiento=patient_data.fecha_nacimiento,  # Uso correcto de patient_data
                obrasocial=patient_data.obrasocial,  # Uso correcto de patient_data
                medico=medico  # Asignar médico usando el objeto encontrado
            )
        except TransactionIntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @db_session
    def get_patient(self, patient_id: int):
        # Lógica para obtener un paciente específico
        patient = models.Patient.get(id=patient_id)
        if not patient:
            return None
        return patient.to_dict()

    @db_session
    def get_all_patients(self):
        # Lógica para obtener todos los pacientes
        return [p.to_dict() for p in select(p for p in models.Patient)]

    @db_session
    def update_patient(self, patient_id: int, update_data: schemas.PatientUpdate):
        # Lógica para actualizar un paciente
        patient = models.Patient.get(id=patient_id)
        if not patient:
            return None
        patient.set(**update_data.dict(exclude_unset=True))
        return patient.to_dict()

    @db_session
    def delete_patient(self, dni: str):
        patient = models.Patient.get(dni=dni)  # Buscar paciente por DNI
        if not patient:
            return False  # Retornar False si no se encuentra el paciente
        patient.delete()  # Eliminar el paciente
        return True  # Retornar True si se eliminó correctamente

