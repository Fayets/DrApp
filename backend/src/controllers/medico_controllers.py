from fastapi import HTTPException, APIRouter
from pony.orm import *
from src import schemas
from src.schemas import *
from src.services.medico_services import *
from pydantic import BaseModel
from datetime import date

router = APIRouter()

medico_service = MedicoService


@router.post("/register", response_model=RegisterMessage, status_code=201)
def register_medico(medico: schemas.MedicoCreate):
    try:
        medico_created = medico_service.create_medico(medico)
        return {
            "message": "Medico creado correctamente",
            "success": True,
        }
    except HTTPException as e:
        # Maneja el error y devuelve un mensaje personalizado
        return {
            "message": e.detail,
            "success": False,
        }
    except Exception as e:
        return {
            "message": "Error inesperado al crear el Medico.",
            "success": False,
        }


#Esquema para el login 
class LoginData(BaseModel):
    email: EmailStr
    password: str
    
@router.post("/login")
def login_medico(login_data: LoginData):
    medico = MedicoService.authenticate_medico(login_data.email, login_data.password)
    if not medico:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"msg": "Inicio de sesión exitoso", "medico_id": medico.id}