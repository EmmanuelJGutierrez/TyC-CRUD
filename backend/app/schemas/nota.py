from pydantic import BaseModel
from datetime import date

class NotaBase(BaseModel):
    contenido: str

class NotaCreate(NotaBase):
    id_usuario: int
    id_ticket: int

class NotaResponse(NotaBase):
    id: int
    fecha: date
    id_usuario: int
    id_ticket: int

    class Config:
        from_attributes = True