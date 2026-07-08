from sqlalchemy import ForeignKey, Text, Date
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base

class Nota(Base):
    __tablename__ = 'nota'

    id: Mapped[int] = mapped_column(primary_key=True)
    contenido: Mapped[str] = mapped_column(Text, nullable=False)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)
    id_ticket: Mapped[int] = mapped_column(ForeignKey('ticket.id'), nullable=False)
