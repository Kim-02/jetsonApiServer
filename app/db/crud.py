from datetime import datetime
from sqlalchemy.orm import Session
from app.db import models


def create_sensor(db: Session, sensor_data: dict):
    sensor = models.Sensor(**sensor_data)
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor


def get_sensor_list(db: Session):
    return db.query(models.Sensor).all()


def get_sensor_by_id(db: Session, sen_id: int):
    return db.query(models.Sensor).filter(models.Sensor.sen_id == sen_id).first()


def get_sensor_by_num(db: Session, sen_num: str):
    return db.query(models.Sensor).filter(models.Sensor.sen_num == sen_num).first()


def get_sensors_by_workplace(db: Session, wp_id: int):
    return db.query(models.Sensor).filter(models.Sensor.wp_id == wp_id).all()


def create_th_trans(db: Session, sen_id: int, wp_id: int, temp: float, humd: float, time: datetime | None = None):
    row = models.ThTrans(
        sen_id=sen_id,
        wp_id=wp_id,
        temp=temp,
        humd=humd,
        time=time or datetime.now()
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def create_wd_trans(db: Session, sen_id: int, wp_id: int, sk_temp: float, hr: float, time: datetime | None = None):
    row = models.WdTrans(
        sen_id=sen_id,
        wp_id=wp_id,
        sk_temp=sk_temp,
        hr=hr,
        time=time or datetime.now()
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def create_situ_trans(db: Session, sen_id: int, wp_id: int, detail: str, time: datetime | None = None):
    row = models.SituTrans(
        sen_id=sen_id,
        wp_id=wp_id,
        detail=detail,
        time=time or datetime.now()
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


def get_th_trans_by_workplace(db: Session, wp_id: int):
    return db.query(models.ThTrans).filter(models.ThTrans.wp_id == wp_id).all()


def get_wd_trans_by_workplace(db: Session, wp_id: int):
    return db.query(models.WdTrans).filter(models.WdTrans.wp_id == wp_id).all()


def get_situ_trans_by_workplace(db: Session, wp_id: int):
    return db.query(models.SituTrans).filter(models.SituTrans.wp_id == wp_id).all()