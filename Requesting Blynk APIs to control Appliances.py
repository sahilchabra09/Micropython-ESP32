#Requesting Blynk APIs to control Appliances

import network
import urequests
import time
from machine import Pin

# Initialize variables to manage button state and HTTP request status
but_status = False  # Represents the button state (True for pressed, False for released)
but_flag = 0  # Helps to prevent multiple HTTP requests for the same button press
Status = 0  # Stores the HTTP request status

# Define a Pin object for the button connected to GPIO Pin 0
but = Pin(0, Pin.IN)

# Function to connect to Wi-Fi
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect('ss', 'sms123458956')  # Replace 'ss' and 'sms123458956' with your Wi-Fi SSID and password
    if not wifi.isconnected():
        print('Connecting...')
        timeout = 0
        while (not wifi.isconnected() and timeout < 5):
            print(5 - timeout)
            timeout = timeout + 1
            time.sleep(1)
    if wifi.isconnected():
        print('Connected')

# Interrupt handler function for the button
def buttons_irq(pin):
    global but_status
    global but_flag
    but_status = not but_status  # Toggle the button status from pressed to released or vice versa
    but_flag = 1  # Set the flag to indicate that a button press has occurred

# Attach the interrupt handler to the button's falling edge (button press)
but.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)

# Connect to Wi-Fi
connect_wifi()

# Main loop
while True:
    # Check if the button status has changed and a button press occurred
    if but_status and but_flag == 1:
        # Send an HTTP GET request to turn the light off
        req = urequests.get('http://blynk-cloud.com/fAdFW1gKTybAqa8S21wUAuIFFMvZGyk8/update/V1?value=1')
        but_flag = 0  # Reset the button press flag
        Status = req.status_code  # Get the HTTP request status code
        if Status == 200:
            print("Request successful")
            print("Light Off")
            req.close()  # Close the HTTP request

    elif not but_status and but_flag == 1:
        # Send an HTTP GET request to turn the light on
        req = urequests.get('http://blynk-cloud.com/fAdFW1gKTybAqa8S21wUAuIFFMvZGyk8/update/V1?value=0')
        but_flag = 0  # Reset the button press flag
        Status = req.status_code  # Get the HTTP request status code
        if Status == 200:
            print("Request successful")
            print("Light On")
            req.close()  # Close the HTTP request

            #<Explanation>
""" The code begins by importing the necessary modules: network, urequests, time, and Pin.

Variables are initialized to manage the button state (but_status), button press flag (but_flag), and HTTP request status (Status).

A Pin object, named but, is created to represent the button connected to GPIO Pin 0. It's defined as an input pin.

The connect_wifi function is defined to connect to a Wi-Fi network using the provided SSID and password. It handles the Wi-Fi connection process and prints messages indicating the connection status.

The buttons_irq function serves as the interrupt handler for the button press. It toggles the but_status variable when the button is pressed and sets the but_flag to 1 to indicate a button press.

The but.irq method is used to attach the buttons_irq interrupt handler to the falling edge of the button (when the button is pressed).

The connect_wifi function is called to establish the Wi-Fi connection.

The main loop (while True) continuously checks the button status and the button press flag.

If the button is pressed (but_status is True) and a button press is detected (but_flag is 1), it sends an HTTP request to turn the light off using the Blynk API.

If the button is released (but_status is False) and a button press is detected (but_flag is 1), it sends an HTTP request to turn the light on using the Blynk API.

After sending the HTTP request, the code checks the HTTP response status (Status) to ensure that the request was successful and prints corresponding messages.

The req.close() method is used to close the HTTP request. """            
