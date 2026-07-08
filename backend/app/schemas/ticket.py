from pydantic import BaseModel
from datetime import date
from ..models import Prioridad, Estado

class TicketBase(BaseModel):
    titulo: str
    descripcion: str
    prioridad: Prioridad

class TicketCreate(TicketBase):
    usuario_id: int

class TicketResponse(TicketBase):
    id: int
    estado: Estado
    tecnico_id: int | None
    fecha: date

    class Config:
        from_attributes = True