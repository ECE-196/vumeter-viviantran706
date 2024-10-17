import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

decay_rate = .5
max_volume = 70000
sensitvity = .05
volume_at = 0

def get_volume():
    raw_value = microphone.value
    return volume

def update_leds(volume):
    led_count = len(leds)
    led_on = int( volume * led_count)
    for i in range(led_count):
        leds[i].value = i < led_on


# main loop
while True:
    volume = get_volume()
    print(volume)

    if volume > volume_at:
        display_volume = volume 
    else:
        volume_at = max(0,volume_at - decay_rate)
    update_leds(volume_at)

    print(volume) 
    sleep(0.05)


    
     

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?