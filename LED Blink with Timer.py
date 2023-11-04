# MicroPython LED Blink with Timer
from machine import Timer, Pin

# Initialize the LED on Pin 2 as an output
led = Pin(2, Pin.OUT)

# Create a Timer object with ID 0
timer = Timer(0)

# Initialize the timer with a 1000ms (1 second) period, in periodic mode, and a callback function
# The callback function toggles the LED state each time it's called
timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: led.value(not led.value()))

# The timer will now trigger the callback function every 1 second, toggling the LED state

