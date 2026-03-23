from pydantic import BaseModel
from datetime import datetime
from typing import List


class ThTransResponse(BaseModel):
    sen_id: int
    wp_id: int
    temp: float
    humd: float
    time: datetime

    class Config:
        from_attributes = True


class WdTransResponse(BaseModel):
    sen_id: int
    wp_id: int
    sk_temp: float
    hr: float
    time: datetime

    class Config:
        from_attributes = True


class SituTransResponse(BaseModel):
    sen_id: int
    wp_id: int
    detail: str
    time: datetime

    class Config:
        from_attributes = True