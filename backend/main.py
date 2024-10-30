import uvicorn
from fastapi import FastAPI #importamos la funciones de FastAPI
from src.db import db
from src.controllers.medico_controllers import router as medico_router
from src.controllers.patient_controller import router as patient_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #creamos una instancia. Este será el punto de interacción principal para crear todo tu API.

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)

# Mapeando las entidades a tablas (si no existe la tabla, la crea)
db.generate_mapping(create_tables=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia a tu dominio específico en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Lista de Rutas

#Medico

app.include_router(medico_router, prefix="/medico", tags=["medico"])

#Paciente

app.include_router(patient_router, prefix="/paciente", tags=["paciente"])






