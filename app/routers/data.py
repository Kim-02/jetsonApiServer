from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.db import crud
from app.schemas.data import (
    ThTransResponse,
    WdTransResponse,
    SituTransResponse,
)

router = APIRouter(prefix="/api/data", tags=["Sensor Data"])


@router.get("/th/workplace/{wp_id}", response_model=List[ThTransResponse], summary="작업장별 온습도 데이터 조회")
def get_th_data(wp_id: int, db: Session = Depends(get_db)):
    return crud.get_th_trans_by_workplace(db, wp_id)


@router.get("/wd/workplace/{wp_id}", response_model=List[WdTransResponse], summary="작업장별 워치 데이터 조회")
def get_wd_data(wp_id: int, db: Session = Depends(get_db)):
    return crud.get_wd_trans_by_workplace(db, wp_id)


@router.get("/situ/workplace/{wp_id}", response_model=List[SituTransResponse], summary="작업장별 상황 데이터 조회")
def get_situ_data(wp_id: int, db: Session = Depends(get_db)):
    return crud.get_situ_trans_by_workplace(db, wp_id)