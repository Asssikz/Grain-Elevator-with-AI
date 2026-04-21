from Helpers.helpers import periodic
from pibody import Climate, Distance
from config import ELEVATOR_PINS

climate = Climate(ELEVATOR_PINS["climate"])
distance = Distance(ELEVATOR_PINS["distance"])

telemetry = {
    "temp": None,
    "humidity": None,
    "distance": None,
}

@periodic(10)
def get_telemetry():
    telemetry["temp"] = round(climate.read_temperature(), 1)
    telemetry["hum"] = round(climate.read_humidity(), 1)
    telemetry["distance"] = round(distance.read(), 1)
    return telemetry