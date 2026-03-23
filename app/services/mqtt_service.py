import json
from datetime import datetime
from app.db.database import SessionLocal
from app.db import crud


def handle_sensor_message(topic: str, payload: str):
    """
    payload 예시
    1) 온습도:
    {
      "sen_id": 1,
      "wp_id": 1,
      "type": "TH",
      "temp": 29.5,
      "humd": 61.2,
      "time": "2026-03-23T13:20:00"
    }

    2) 워치:
    {
      "sen_id": 2,
      "wp_id": 1,
      "type": "WD",
      "sk_temp": 36.4,
      "hr": 91,
      "time": "2026-03-23T13:20:00"
    }

    3) 상황:
    {
      "sen_id": 3,
      "wp_id": 1,
      "type": "SITU",
      "detail": "작업자 접근 위험 감지",
      "time": "2026-03-23T13:20:00"
    }
    """
    data = json.loads(payload)
    db = SessionLocal()

    try:
        msg_time = datetime.fromisoformat(data["time"]) if "time" in data else datetime.now()
        msg_type = data["type"]

        if msg_type == "TH":
            crud.create_th_trans(
                db=db,
                sen_id=data["sen_id"],
                wp_id=data["wp_id"],
                temp=data["temp"],
                humd=data["humd"],
                time=msg_time,
            )

        elif msg_type == "WD":
            crud.create_wd_trans(
                db=db,
                sen_id=data["sen_id"],
                wp_id=data["wp_id"],
                sk_temp=data["sk_temp"],
                hr=data["hr"],
                time=msg_time,
            )

        elif msg_type == "SITU":
            crud.create_situ_trans(
                db=db,
                sen_id=data["sen_id"],
                wp_id=data["wp_id"],
                detail=data["detail"],
                time=msg_time,
            )

    finally:
        db.close()