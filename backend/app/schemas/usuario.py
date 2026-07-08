from pydantic import BaseModel, EmailStr
from datetime import date

class UsuarioBase(BaseModel):
    usuario: str
    correo: EmailStr
    fechanacimiento: date
    genero: str
    rol: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True