from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from ..schemas import UsuarioCreate
from ..database import get_db
from ..models import Usuario


db_dependencies = Annotated [Session, Depends(get_db)]

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Usuario no encontrado"}},)

@router.get("/{usuario_id}")
async def leer_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    return usuario

@router.post("/")
async def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = Usuario(
        usuario=usuario.usuario,
        correo=usuario.correo,
        fechanacimiento=usuario.fechanacimiento,
        genero=usuario.genero,
        rol=usuario.rol,
        password_hash=usuario.password
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return {"mensaje": "Usuario creado", "usuario": db_usuario}

@router.put("/{usuario_id}")
async def actualizar_usuario(usuario_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        return {"mensaje": "Usuario no encontrado"}
    db_usuario.usuario = usuario.usuario
    db_usuario.correo = usuario.correo
    db_usuario.fechanacimiento = usuario.fechanacimiento
    db_usuario.genero = usuario.genero
    db_usuario.rol = usuario.rol
    db_usuario.password_hash = usuario.password
    db.commit()
    db.refresh(db_usuario)
    return {"mensaje": "Usuario actualizado exitosamente", "usuario": db_usuario}

@router.delete("/{usuario_id}")
async def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        return {"mensaje": "Usuario no encontrado"}
    db.delete(db_usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado exitosamente"}
