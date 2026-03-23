from fastapi import APIRouter
from datetime import datetime
from app.schemas.system import HealthResponse, JetsonInfoResponse

router = APIRouter(prefix="/api", tags=["System"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="서버 상태 확인",
    description="Jetson 내부 API 서버의 동작 여부를 확인합니다."
)
def get_health():
    return HealthResponse(
        status="ok",
        server_time=datetime.now()
    )


@router.get(
    "/info",
    response_model=JetsonInfoResponse,
    summary="Jetson 기본 정보 조회",
    description="앱이 Jetson 등록 전에 표시할 허브 정보를 조회합니다."
)
def get_info():
    return JetsonInfoResponse(
        device_id="jetson-orin-nx-01",
        hostname="jetsonhub_tcp.local",
        ip_address="192.168.0.10",
        port=8000,
        mqtt_broker="mqtt://192.168.0.10:1883",
        api_version="1.0.0",
        site_name="siteA"
    )