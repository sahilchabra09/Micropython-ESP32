import network

# Create a WLAN (Wireless LAN) interface in access point mode (AP_IF).
wifi = network.WLAN(network.AP_IF)

# Enable the WLAN interface to turn on the access point.
wifi.active(True)

# Configure the access point with the desired SSID, password, and authentication mode.
wifi.config(essid='techiesms', password='12345678', authmode=network.AUTH_WPA_WPA2_PSK)

# Retrieve and print the network configuration of the access point.
print(wifi.ifconfig())

'''The network.AP_IF is used to create a WLAN interface in access point mode.
wifi.active(True) is used to enable the access point.
wifi.config() is used to configure the access point with the SSID, password, and authentication mode.
wifi.ifconfig() is used to retrieve the network configuration, including the IP address, subnet mask, gateway, etc''.
