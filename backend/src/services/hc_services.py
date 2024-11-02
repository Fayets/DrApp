from pony.orm import db_session, select
from src.models import HistoriaClinica, Patient
from src.schemas import HistoriaClinicaCreate, HistoriaClinicaUpdate, PacienteResponse
from fastapi import HTTPException

class HistoriaClinicaService:
    @db_session
    def crear_historia_clinica(self, dni: str, historia_clinica_data: HistoriaClinicaCreate):
        paciente = Patient.get(dni=dni)
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        
        historia_clinica = HistoriaClinica(
            paciente=paciente,
            fecha_creacion=historia_clinica_data.fecha_creacion,
            alergias=historia_clinica_data.alergias,
            condiciones=historia_clinica_data.condiciones,
            observaciones=historia_clinica_data.observaciones,
            prescripciones=historia_clinica_data.prescripciones
        )
        
        return historia_clinica

    @db_session
    def actualizar_historia_clinica_por_dni(self, dni: str, historia_clinica_data: HistoriaClinicaUpdate):
        paciente = Patient.get(dni=dni)
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")
        
        historia_clinica = HistoriaClinica.get(paciente=paciente)
        if not historia_clinica:
            raise HTTPException(status_code=404, detail="Historia clínica no encontrada para el paciente")

        if historia_clinica_data.alergias is not None:
            historia_clinica.alergias = historia_clinica_data.alergias
        if historia_clinica_data.condiciones is not None:
            historia_clinica.condiciones = historia_clinica_data.condiciones
        if historia_clinica_data.observaciones is not None:
            historia_clinica.observaciones = historia_clinica_data.observaciones
        if historia_clinica_data.prescripciones is not None:
            historia_clinica.prescripciones = historia_clinica_data.prescripciones

        return historia_clinica
    
    @db_session
    def obtener_paciente_con_historia(self, dni: str):
        paciente = Patient.get(dni=dni)
        if not paciente:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")

        historias_clinicas = select(hc for hc in HistoriaClinica if hc.paciente == paciente)[:]
        
        return {
            "id": paciente.id,
            "nombre": paciente.nombre,
            "apellido": paciente.apellido,
            "dni": paciente.dni,
            "fecha_nacimiento": paciente.fecha_nacimiento,
            "obrasocial": paciente.obrasocial,
            "medico_id": paciente.medico.id,  # Cambiado para coincidir con el schema
            "historias_clinicas": [{
                "id": hc.id,
                "fecha_creacion": hc.fecha_creacion,
                "alergias": hc.alergias,
                "condiciones": hc.condiciones,
                "observaciones": hc.observaciones,
                "prescripciones": hc.prescripciones,
            } for hc in historias_clinicas]
        }