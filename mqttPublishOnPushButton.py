# Adapted from: https://github.com/mrichardson23/garage-indicator
import network
import config # network = "" network_password = "" mqtt_server_address = ""
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.network, config.network_password)

import mip
mip.install("umqtt.simple")

from umqtt.simple import MQTTClient
import time
from machine import Pin, reset
import utime


while not wlan.isconnected():
    pass

print("Connected to Wifi.")

mqtt_server = '192.168.1.137:1883'
client_id = 'Pico'
topic_pub = b'/homeass'

def mqtt_connect():
    #client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client = MQTTClient(client_id='PicoTest', server='192.168.1.136', port=1883, user="MQTTUser", password="MQTTUserPassword")
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

client = mqtt_connect()


led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.value(1)
        message = b'TestFromPico Push Button'
        client.publish(topic_pub, message, retain=True)
        time.sleep(0.5)
        led.value(0)
