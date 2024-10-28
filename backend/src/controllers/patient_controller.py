from fastapi import APIRouter, HTTPException
from src.services.patient_services import PatientService
from src.schemas import PatientCreate, PatientUpdate, PacienteResponse  

router = APIRouter()

patient_service = PatientService()

@router.post("/create", response_model=PacienteResponse) 
async def create_patient(patient_data: PatientCreate): 
    return patient_service.create_patient(patient_data)

@router.get("/get/{patient_id}")
def get_patient(patient_id: int):
    patient = patient_service.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient

@router.get("/get_all")
def get_all_patients():
    return patient_service.get_all_patients()

@router.put("/update/{patient_id}")
def update_patient(patient_id: int, patient_update: PatientUpdate):
    updated_patient = patient_service.update_patient(patient_id, patient_update)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return updated_patient

@router.delete("/delete/{dni}", status_code=204)
def delete_patient(dni: str):
    if not patient_service.delete_patient(dni):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"message": "Paciente eliminado correctamente"}

