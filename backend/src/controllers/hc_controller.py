from fastapi import APIRouter, HTTPException
from src.schemas import HistoriaClinicaCreate, HistoriaClinicaResponse, HistoriaClinicaUpdate, PacienteResponse
from src.services.hc_services import HistoriaClinicaService

router = APIRouter()
hc_service = HistoriaClinicaService()

@router.post("/create")
async def crear_historia_clinica(dni: str, historia_clinica: HistoriaClinicaCreate):
    try:
        nueva_historia = hc_service.crear_historia_clinica(dni=dni, historia_clinica_data=historia_clinica)
        return {"Historia clinica creada con exito.": True, "historia": nueva_historia}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update/{dni}", response_model=HistoriaClinicaResponse)
async def update_historia_clinica_por_dni(dni: str, historia_clinica_data: HistoriaClinicaUpdate):
    try:
        updated_historia = hc_service.actualizar_historia_clinica_por_dni(dni, historia_clinica_data)
        return updated_historia
    except HTTPException as e:
        raise e
    
@router.get("/get/{dni}", response_model=PacienteResponse)
async def get_paciente_con_historia(dni: str):
    try:
        paciente_info = hc_service.obtener_paciente_con_historia(dni)
        return paciente_info
    except HTTPException as e:
        raise e