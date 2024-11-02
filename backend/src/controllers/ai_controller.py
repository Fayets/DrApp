# from fastapi import APIRouter, HTTPException
# from src.services.ai_services import AIService  # Asegúrate de importar el AIService
# from src.services.hc_services import HistoriaClinicaService

# router = APIRouter()
# ai_service = AIService()  # Instancia del servicio de AI
# hc_service = HistoriaClinicaService()  # Instancia del servicio de Historia Clínica

# @router.get("/diagnostico/{dni}")
# async def diagnosticar_por_dni(dni: str):
#     try:
#         paciente_info = hc_service.obtener_paciente_con_historia(dni)
#         # Combina las observaciones de todas las historias clínicas
#         historia_clinica = " ".join(hc['observaciones'] for hc in paciente_info['historias_clinicas'])  
#         diagnostico = ai_service.diagnosticar_historia_clinica(historia_clinica)
#         return {"diagnostico": diagnostico}
#     except HTTPException as e:
#         raise e
