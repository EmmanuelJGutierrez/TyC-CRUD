from fastapi import FastAPI
from .models import Nota, Usuario, Ticket
from .database import engine, Base
from .routes import usuario, ticket, nota

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario.router)
app.include_router(ticket.router)
app.include_router(nota.router)