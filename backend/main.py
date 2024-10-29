from fastapi import FastAPI #importamos la funciones de FastAPI
from src.db import db
import uvicorn
from src.controllers.medico_controllers import router as medico_router
from src.controllers.patient_controller import router as patient_router

app = FastAPI() #creamos una instancia. Este será el punto de interacción principal para crear todo tu API.

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)


# Mapeando las entidades a tablas (si no existe la tabla, la crea)
db.generate_mapping(create_tables=True)

#Lista de Rutas

#Medico

app.include_router(medico_router, prefix="/medico", tags=["medico"])

#Medico

app.include_router(patient_router, prefix="/paciente", tags=["paciente"])


