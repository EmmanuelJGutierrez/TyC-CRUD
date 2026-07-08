from sqlalchemy import String, Date
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    correo: Mapped[str] = mapped_column(String(254), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(60), nullable=False)
    fechanacimiento: Mapped [date] = mapped_column(Date, nullable=False)
    genero: Mapped[str] = mapped_column(String(1), nullable=False)
    rol: Mapped[str] = mapped_column(String(20), nullable=False, default='usuario')
    