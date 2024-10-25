from fastapi import FastAPI #importamos la funciones de FastAPI

app = FastAPI() #creamos una instancia. Este será el punto de interacción principal para crear todo tu API.


@app.get("/")
async def root():
    return {"message": "Hello Facu"}