""" 
Config file for the whole project
"""

from micropython import const


## ================================================
## Pico Central
## ================================================

### ====== BLE configuration ======
BLE_SCALES = "Scales Pico"
BLE_ELEVATOR = "Elevator Pico"

BLE_NAMES = {
    "scales": BLE_SCALES,
    "elevator": BLE_ELEVATOR,
}
### ====== BLE configuration ======

### ====== Modules configuration ======
LED_PIN = "D"
BUTTON_PIN = "E"
### ====== Modules configuration ======

### ====== I2S and Audio CONFIGURATION ======
SCK_PIN                  = const(0)
WS_PIN                   = const(1)
SD_PIN                   = const(2)
I2S_ID                   = const(0)
BUFFER_LENGTH_IN_BYTES   = const(16000)

WAV_SAMPLE_SIZE_IN_BITS  = const(16)
SAMPLE_RATE_IN_HZ        = const(16000)
NUM_CHANNELS             = const(1)
WAV_SAMPLE_SIZE_IN_BYTES = const(WAV_SAMPLE_SIZE_IN_BITS // 8)

I2S_CONFIG = {
    'sck': SCK_PIN, 
    'ws': WS_PIN, 
    'sd': SD_PIN, 
    'id': I2S_ID, 
    'buffer_length': BUFFER_LENGTH_IN_BYTES,
    'bits': WAV_SAMPLE_SIZE_IN_BITS, 
    'rate': SAMPLE_RATE_IN_HZ, 
    'ibuf': 4096,
    'nch': NUM_CHANNELS}
### ====== I2S and Audio CONFIGURATION ======
