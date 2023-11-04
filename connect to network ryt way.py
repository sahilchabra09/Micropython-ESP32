import network
import time

timeout = 0
wifi = network.WLAN(network.STA_IF)

# Disable and re-enable the Wi-Fi interface to restart it.
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

# Attempt to connect to the Wi-Fi network with the specified SSID and password.
wifi.connect('Arc', 'qwerty0902')

if not wifi.isconnected():
    print('Connecting...')

    # Try to connect and wait for a connection with a timeout of 5 seconds.
    while (not wifi.isconnected() and timeout <= 5):
        print(f'Timeout: {timeout}')
        timeout = timeout + 1
        time.sleep(1)

    if wifi.isconnected():
        print('Connected')
    else:
        print('worng wifi credentials')

''' The code first disables and re-enables the Wi-Fi interface to restart it. This can be useful in case there are issues with the Wi-Fi connection.

It attempts to connect to the Wi-Fi network with the specified SSID and password using wifi.connect('Smjiofi', 'sms123458956').

If the initial connection attempt is unsuccessful (i.e., wifi.isconnected() returns False), it enters a loop to repeatedly check for a connection and waits for a maximum of 5 seconds (timeout < 5).

The timeout value is incremented within the loop, and there is a 1-second delay between each check using time.sleep(1).

Once a connection is established (as confirmed by wifi.isconnected()), it prints 'Connected.' If the timeout is reached and no connection is made, it prints 'Timeout.'''
