from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from ..schemas import NotaCreate
from ..database import get_db
from ..models import Nota
from datetime import date

db_dependencies = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/notas",
    tags=["notas"],
    responses={404: {"description": "Nota no encontrada"}},
)
@router.get("/{nota_id}")
async def leer_nota(nota_id: int, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id == nota_id).first()
    return nota

@router.post("/")
async def crear_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    db_nota = Nota(
        contenido=nota.contenido,
        id_ticket=nota.id_ticket,
        id_usuario=nota.id_usuario,
        fecha=date.today()
    )
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return {"mensaje": "Nota creada", "nota": db_nota}

@router.put("/{nota_id}")
async def actualizar_nota(nota_id: int, nota: NotaCreate, db: Session = Depends(get_db)):
    db_nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if db_nota is None:
        return {"mensaje": "Nota no encontrada"}
    db_nota.contenido = nota.contenido
    db_nota.id_ticket = nota.id_ticket
    db_nota.id_usuario = nota.id_usuario
    db.commit()
    db.refresh(db_nota)
    return {"mensaje": "Nota actualizada exitosamente", "nota": db_nota}

@router.delete("/{nota_id}")
async def eliminar_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = db.query(Nota).filter(Nota.id == nota_id).first()
    if db_nota is None:
        return {"mensaje": "Nota no encontrada"}
    db.delete(db_nota)
    db.commit()
    return {"mensaje": "Nota eliminada exitosamente"}