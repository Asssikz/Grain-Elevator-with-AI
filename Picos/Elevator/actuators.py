from Helpers.helpers import periodic
from pibody import LED, LEDTower
from config import ELEVATOR_PINS
from telemetry import telemetry

heater = LEDTower(ELEVATOR_PINS["heater"])
air = LED(ELEVATOR_PINS["air"])

actuator_state = {
    "air": False,
    "cooler": False,
}

auto_mode_state = { 
    "air": True,
    "cooler": True,
}

treshold = {
    "air_low": 60,
    "cooler": 25.0,
}

# API for actuators
def air_on():
    air.on()
    actuator_state["air"] = True
    auto_mode_state["air"] = False
    return actuator_state

def air_off():
    air.off()
    actuator_state["air"] = False
    auto_mode_state["air"] = False
    return actuator_state

def cooler_on():
    heater.fill((0, 255, 255)) 
    heater.show()
    actuator_state["cooler"] = True
    auto_mode_state["cooler"] = False
    return actuator_state

def cooler_off():
    heater.fill((0, 0, 0))
    heater.show()
    actuator_state["cooler"] = False
    auto_mode_state["cooler"] = False
    return actuator_state

def auto_mode_on():
    auto_mode_state["air"] = True
    auto_mode_state["cooler"] = True
    return auto_mode_state

def auto_mode_off():
    auto_mode_state["air"] = False
    auto_mode_state["cooler"] = False
    return auto_mode_state

# Inner functions
def _air_on():
    air.on()
    actuator_state["air"] = True

def _air_off():
    air.off()
    actuator_state["air"] = False

def _cooler_on():
    heater.fill((0, 255, 255))
    heater.show()
    actuator_state["cooler"] = True

def _cooler_off():
    heater.fill((0, 0, 0)) 
    heater.show()
    actuator_state["cooler"] = False

@periodic(10)
def auto_mode():
    if auto_mode_state["air"]:
        if telemetry["hum"] > treshold["air"]:
            _air_on()
        elif telemetry["hum"] < treshold["air"]:
            _air_off()
    if auto_mode_state["cooler"]:
        if telemetry["temp"] < treshold["cooler"]:
            _cooler_on()
        elif telemetry["temp"] > treshold["cooler"]:
            _cooler_off()
