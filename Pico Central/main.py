from hinter import *
from Helpers.BLE import Central

central = Central(["PICO_B"])

@central.on_read
def on_read(data):
    print(data)

central.start()

while True:
    pass