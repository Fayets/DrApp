from fastapi import HTTPException, APIRouter
from pony.orm import *
from src import schemas
from src.schemas import *
from src.services.medico_services import *
from pydantic import BaseModel
from datetime import date