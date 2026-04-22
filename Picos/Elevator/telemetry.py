from pibody import Climate, Distance
from config import ELEVATOR_PINS

telemetry = {
    "temp": None,
    "humidity": None,
    "distance": None,
}

try:
    climate = Climate(ELEVATOR_PINS["climate"])
except:
    """Mock climate data"""
    climate = None
    telemetry["temp"] = 24.5
    telemetry["hum"] = 40.0

try:
    distance = Distance(ELEVATOR_PINS["distance"])
except:
    """Mock distance data"""
    distance = None
    telemetry["distance"] = 70

def get_telemetry():
    if climate is not None:
        telemetry["temp"] = round(climate.read_temperature(), 1)
        telemetry["hum"] = round(climate.read_humidity(), 1)
    if distance is not None:
        telemetry["distance"] = round(distance.read(), 1)
    return telemetry