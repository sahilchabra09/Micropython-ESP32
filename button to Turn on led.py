#MicroPython Boot Button-Controlled LED
import machine
import time

LED = machine.Pin(2, machine.Pin.OUT)
BUT = machine.Pin(0, machine.Pin.IN)

while True:
    but_status = BUT.value()  # Use a single '=' for assignment
    if but_status == False:  # You can simplify this as "if not but_status:"
        LED.value(1)
    else:
        LED.value(0)

