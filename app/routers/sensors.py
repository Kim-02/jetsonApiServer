from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.db import crud
from app.schemas.sensor import (
    ReadySensorsResponse,
    SensorCreateRequest,
    SensorResponse,
)
from app.schemas.common import MessageResponse
from app.services.discovery_service import (
    start_discovery,
    stop_discovery,
    get_ready_sensors,
)

router = APIRouter(prefix="/api/sensors", tags=["Sensors"])


@router.post("/discovery/start", response_model=MessageResponse, summary="센서 탐지 시작")
def start_sensor_discovery():
    start_discovery()
    return {"message": "sensor discovery started"}


@router.post("/discovery/stop", response_model=MessageResponse, summary="센서 탐지 종료")
def stop_sensor_discovery():
    stop_discovery()
    return {"message": "sensor discovery stopped"}


@router.get("/ready", response_model=ReadySensorsResponse, summary="대기 센서 목록 조회")
def get_sensors_ready():
    return {"sensors": get_ready_sensors()}


@router.post("", response_model=SensorResponse, status_code=201, summary="센서 등록")
def create_sensor(request: SensorCreateRequest, db: Session = Depends(get_db)):
    exists = crud.get_sensor_by_num(db, request.sen_num)
    if exists:
        raise HTTPException(status_code=409, detail="sensor product number already exists")

    sensor = crud.create_sensor(db, request.model_dump())
    return sensor


@router.get("", response_model=List[SensorResponse], summary="등록된 센서 전체 조회")
def get_sensor_list(db: Session = Depends(get_db)):
    return crud.get_sensor_list(db)


@router.get("/workplace/{wp_id}", response_model=List[SensorResponse], summary="작업장별 센서 조회")
def get_sensor_list_by_workplace(wp_id: int, db: Session = Depends(get_db)):
    return crud.get_sensors_by_workplace(db, wp_id)


@router.get("/{sen_id}", response_model=SensorResponse, summary="센서 상세 조회")
def get_sensor_detail(sen_id: int, db: Session = Depends(get_db)):
    sensor = crud.get_sensor_by_id(db, sen_id)
    if not sensor:
        raise HTTPException(status_code=404, detail="sensor not found")
    return sensor