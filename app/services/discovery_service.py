from typing import Dict

discovered_sensors: Dict[str, dict] = {
    "hr-band-001": {
        "device_key": "hr-band-001",
        "sensor_type": "HR",
        "name": "작업자 심박 밴드 1",
        "manufacturer": "Custom",
        "product_number": "HR-0001",
        "topic": "siteA/discovery/hr-band-001",
        "status": "discovered",
    },
    "temp-hum-001": {
        "device_key": "temp-hum-001",
        "sensor_type": "TH",
        "name": "무선 온습도계 1",
        "manufacturer": "Custom",
        "product_number": "TH-0001",
        "topic": "siteA/discovery/temp-hum-001",
        "status": "discovered",
    },
}

discovery_running = False


def start_discovery():
    global discovery_running
    discovery_running = True


def stop_discovery():
    global discovery_running
    discovery_running = False


def get_ready_sensors():
    return list(discovered_sensors.values())