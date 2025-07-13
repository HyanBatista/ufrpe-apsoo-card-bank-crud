from fastapi import FastAPI

from app.api.v1.routes import bank
from app.db.session import lifespan

app = FastAPI(
    title="UFRPE APSOO Card Bank CRUD",
    description="A simple CRUD application for managing credit cards and bank accounts.",
    version="1.0.0",
    lifespan=lifespan,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(bank.router, prefix="/api/v1", tags=["bank"])
