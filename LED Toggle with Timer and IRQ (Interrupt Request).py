#MicroPython Button-Triggered LED Toggle with Timer and IRQ (Interrupt Request)
from machine import Timer, Pin

# Initialize the LED on Pin 2 as an output
led = Pin(2, Pin.OUT)

# Initialize the button on Pin 0 as an input
but = Pin(0, Pin.IN)

# Define the callback function for button interrupts
def buttons_irq(pin):
    print("Button pressed")  # You can modify this message as needed
    led.value(not led.value())

# Initialize a Timer object with ID 0
timer = Timer(0)

# Initialize the timer with a 1000ms (1 second) period, in periodic mode, and a callback function
timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t: led.value(not led.value()))

# Set up the button to trigger the callback function on a falling edge IRQ (Interrupt Request)
but.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)

# The timer will now toggle the LED state every 1 second, and the button press will also toggle the LED state

