import machine
import time

LED = machine.Pin(2,machine.Pin.OUT)

while True:
    LED.value(1)
    time.sleep(0.5)
    LED.value(0)
    time.sleep(0.5)
    

