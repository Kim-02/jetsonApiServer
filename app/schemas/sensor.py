from pydantic import BaseModel, Field
from typing import List


class DiscoveredSensor(BaseModel):
    device_key: str
    sensor_type: str
    name: str
    manufacturer: str | None = None
    product_number: str | None = None
    topic: str
    status: str


class ReadySensorsResponse(BaseModel):
    sensors: List[DiscoveredSensor]


class SensorCreateRequest(BaseModel):
    sen_dept: str = Field(..., example="HR")
    sen_cr: str = Field(..., example="Custom")
    sen_nm: str = Field(..., example="심박 체크 밴드")
    sen_num: str = Field(..., example="HR-0001")
    sen_mnum: int = Field(..., example=1001)
    wp_id: int = Field(..., example=1)


class SensorResponse(BaseModel):
    sen_id: int
    sen_dept: str
    sen_cr: str
    sen_nm: str
    sen_num: str
    sen_mnum: int
    wp_id: int

    class Config:
        from_attributes = True