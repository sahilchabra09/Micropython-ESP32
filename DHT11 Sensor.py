# MicroPython DHT11 Temperature and Humidity Sensor
from machine import Pin
import dht
import time

sensor_data = dht.DHT11(Pin(15))

def call_dht():
    sensor_data.measure()
    temp = sensor_data.temperature()
    hum = sensor_data.humidity()
    print('Temperature - ', temp, 'Humidity - ', hum)

while True:
    call_dht()
    time.sleep(1)
