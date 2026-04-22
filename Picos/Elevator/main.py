import time
from Helpers.helpers import periodic
from Picos.Elevator.BLE import BLETransport
from Picos.Elevator.actuators import (
    air_on,
    air_off,
    cooler_on,
    cooler_off,
    light_on,
    light_off,
    auto_on,
    auto_off,
    auto_mode,
    actuator_state,
)
from Picos.Elevator.telemetry import telemetry, get_telemetry


def _b(value):
    return 1 if value else 0


def build_payload():
    return {
        "tel": {
            "t": telemetry.get("temp"),
            "h": telemetry.get("hum"),
            "d": telemetry.get("distance"),
        },
        "act": {
            "a": _b(actuator_state.get("air")),
            "c": _b(actuator_state.get("cooler")),
        },
    }


def command_handler(cmd):
    commands = {
        "air_on()": air_on,
        "air_off()": air_off,
        "cooler_on()": cooler_on,
        "cooler_off()": cooler_off,
        "light_on()": light_on,
        "light_off()": light_off,
        "auto_on()": auto_on,
        "auto_off()": auto_off,
    }
    fn = commands.get(cmd)
    if fn is None:
        print("[CMD] Unknown command:", cmd)
        return
    fn()
    print("[CMD] Done. State:", actuator_state)


def main():
    ble = BLETransport(
        name="ElevatorPico",
        mode="peripheral",
        notify_interval_ms=500,
        command_handler=command_handler,
        payload_provider=build_payload,
    )
    ble.start()

    @periodic(10)
    def thread_task(timer):
        get_telemetry()
        auto_mode()

    while True:
        ble.tick()
        time.sleep_ms(50)