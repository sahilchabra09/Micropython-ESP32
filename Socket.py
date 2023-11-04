# To turn on and off the internal led of ESP32 module using a website 
import machine
import usocket as socket
import time
import network

# Initialize a timeout variable for WiFi connection
timeout = 0

# Create a network.WLAN object to manage the WiFi connection
wifi = network.WLAN(network.STA_IF)

# Restart WiFi by disabling and re-enabling it
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

# Connect to a WiFi network with SSID 'SmS_jiofi' and password 'sms123458956'
wifi.connect('SmS_jiofi', 'sms123458956')

if not wifi.isconnected():
    print('Connecting...')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)

if wifi.isconnected():
    print('Connected to the network')
    print('Network configuration:', wifi.ifconfig())

# HTML Document
html = '''<!DOCTYPE html>
<html>
<center><h2>ESP32 Webserver</h2></center>
<form>
<center>
<h3>LED</h3>
<button name="LED" value='ON' type='submit'>ON</button>
<button name="LED" value='OFF' type='submit'>OFF</button>
</center>
'''

# Output Pin Declaration
LED = machine.Pin(2, machine.Pin.OUT)
LED.value(0)  # Initialize the LED pin to the OFF state (0)

# Initializing a socket for the web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

Host = ''  # An empty string allows connections from all IP addresses
Port = 80  # Port 80 is used for HTTP
s.bind((Host, Port))  # Bind the socket to the host and port

s.listen(5)  # Listen for up to 5 clients simultaneously

# Main loop
while True:
    connection_socket, address = s.accept()  # Accept a new connection and get the socket and address of the client
    print("Got a connection from", address)
    request = connection_socket.recv(1024)  # Receive the client's request, up to 1024 bytes
    print("Content", request)  # Print the received request
    request = str(request)  # Convert the request from bytes to a string

    # Check if the request contains '/?LED=ON' or '/?LED=OFF' indicating an LED control request
    LED_ON = request.find('/?LED=ON')
    LED_OFF = request.find('/?LED=OFF')

    # If '/?LED=ON' is found in the request, turn the LED ON (LED pin set to 1)
    if LED_ON == 6:
        LED.value(1)

    # If '/?LED=OFF' is found in the request, turn the LED OFF (LED pin set to 0)
    if LED_OFF == 6:
        LED.value(0)

    # Send the HTML document as a response to all connected clients
    response = html
    connection_socket.send(response)

    # Close the connection socket for this client
    connection_socket.close()


''' The code sets up a simple web server on an ESP32 microcontroller to control an LED. It first handles the WiFi connection, and then it listens for incoming client connections to control the LED via a web interface.

The ESP32 WiFi connection is established using the network.WLAN module. It attempts to connect to a WiFi network with SSID 'SmS_jiofi' and password 'sms123458956'. It also handles connection retries and prints the network configuration when connected.

An HTML document (html) is defined, which serves as the web interface to control the LED. Two buttons, 'ON' and 'OFF,' are provided.

The code initializes an output pin (LED) connected to GPIO Pin 2, which is used to control the LED. It starts with the LED turned off (0).

A socket (s) is created for the web server, using Internet sockets (AF_INET) and the TCP protocol (SOCK_STREAM). The server binds to host '' (allowing all IP addresses) and port 80 (HTTP).

The main loop starts listening for incoming client connections using the s.listen(5) call. It can handle up to 5 clients simultaneously.

When a client connects, it accepts the connection, receives the client's request, and parses it.

The code checks the request for '/?LED=ON' and '/?LED=OFF' strings, indicating LED control requests. If '/?LED=ON' is found, the LED is turned on (LED pin set to 1). If '/?LED=OFF' is found, the LED is turned off (LED pin set to 0).

The HTML document (html) is sent as a response to the client, providing the buttons to control the LED.

Finally, the connection socket is closed for that client, and the code continues listening for new connections. '''    
