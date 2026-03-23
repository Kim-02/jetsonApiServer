from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import sensors, system, data
from app.db import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Jetson Edge Hub API",
    version="2.0.0",
    description="MQTT discovery + DB 저장 기반 Jetson Hub API"
)

app.include_router(system.router)
app.include_router(sensors.router)
app.include_router(data.router)