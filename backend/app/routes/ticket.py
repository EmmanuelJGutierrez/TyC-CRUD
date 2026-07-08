from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from ..schemas import TicketCreate
from ..database import get_db
from ..models import Ticket, Estado, Nota
from datetime import date

db_dependencies = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix = "/tickets",
    tags = ["tickets"],
    responses = {404: {"description": "Ticket no encontrado"}},
)
@router.get("/{ticket_id}")
async def leer_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    return ticket

@router.post("/")
async def crear_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(
        titulo=ticket.titulo,
        descripcion=ticket.descripcion,
        estado=Estado.e1,
        prioridad=ticket.prioridad,
        usuario_id=ticket.usuario_id,
        fecha=date.today()
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return {"mensaje": "Ticket creado", "ticket": db_ticket}

@router.put("/{ticket_id}")
async def actualizar_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket is None:
        return {"mensaje": "Ticket no encontrado"}
    db_ticket.titulo = ticket.titulo
    db_ticket.descripcion = ticket.descripcion
    db_ticket.prioridad = ticket.prioridad
    db_ticket.usuario_id = ticket.usuario_id
    db.commit()
    db.refresh(db_ticket)
    return {"mensaje": "Ticket actualizado exitosamente", "ticket": db_ticket}

@router.delete("/{ticket_id}")
async def eliminar_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket is None:
        return {"mensaje": "Ticket no encontrado"}
    db.query(Nota).filter(Nota.id_ticket == ticket_id).delete(synchronize_session=False)    
    db.delete(db_ticket)
    db.commit()
    return {"mensaje": "Ticket eliminado exitosamente"}