# Import the 'network' module to work with Wi-Fi networks.
import network

# Create a WLAN (Wireless LAN) interface in station mode (STAL_IF).
wifi = network.WLAN(network.STA_IF)

# Enable the WLAN interface to turn on Wi-Fi.
wifi.active(True)

# Perform a Wi-Fi network scan to find nearby access points (APs).
networks = wifi.scan()

# Print the list of discovered networks.
print(networks)

'''Import the 'network' module to access Wi-Fi functionality.

Create a WLAN interface object named 'wifi' in station mode (STAL_IF). This allows the ESP32 to connect to existing Wi-Fi networks as a client.

Enable the WLAN interface to turn on the ESP32's Wi-Fi capability using wifi.active(True).

Perform a Wi-Fi scan with wifi.scan() to discover nearby Wi-Fi networks. The results will be stored in the 'networks' variable, which will be a list of dictionaries, each representing a detected network.

Finally, print the list of discovered Wi-Fi networks using print(networks).'''
