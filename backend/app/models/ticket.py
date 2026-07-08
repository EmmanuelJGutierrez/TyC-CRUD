import enum
from sqlalchemy import String, Date, ForeignKey, Text, Enum
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base

class Prioridad(enum.Enum):
    p1 = 'minima'
    p2 = 'baja'
    p3 = 'media'
    p4 = 'alta'
    p5 = 'urgente'

class Estado(enum.Enum):
    e1 = 'enviado'
    e2 = 'abierto'
    e3 = 'en_proceso'
    e4 = 'cerrado'

class Ticket(Base):
    __tablename__ = 'ticket'

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)
    descripcion: Mapped[str] = mapped_column(Text, nullable=False)
    prioridad: Mapped[Prioridad] = mapped_column(nullable=False)
    estado: Mapped[Estado] = mapped_column(nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)
    tecnico_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=True)