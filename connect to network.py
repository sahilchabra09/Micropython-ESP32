import network

# Create a WLAN (Wireless LAN) interface in station mode (STA_IF).
wifi = network.WLAN(network.STA_IF)

# Enable the WLAN interface to turn on Wi-Fi client mode.
wifi.active(True)

# Connect to the Wi-Fi network with the specified SSID and password.
wifi.connect('wifi name', 'password')

# Wait for the Wi-Fi connection to be established.
#prob - If wifi Name or password is wrong it will get stuck in infinte loop 
while not wifi.isconnected():
    pass

# Check if the Wi-Fi connection is established and print the network configuration.
if wifi.isconnected():
    print(wifi.ifconfig())
'''network.STA_IF is used to create a WLAN interface in station mode, allowing your device to connect to an existing Wi-Fi network.

wifi.active(True) is used to enable the Wi-Fi interface to turn on client mode.

wifi.connect('SmS_jiofi', 'sms123458956') is used to initiate the connection to the specified Wi-Fi network with the given SSID and password.

The while not wifi.isconnected(): pass loop is used to wait until the Wi-Fi connection is established. Once connected, the loop will exit.

After the connection is established, wifi.isconnected() is checked to ensure the connection is successful, and if it is, the network configuration is printed using wifi.ifconfig().'''
