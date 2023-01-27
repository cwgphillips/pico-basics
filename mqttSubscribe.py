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

mqtt_server = '192.168.1.136'
mqtt_port = 1883
client_id = 'Pico'
topic_sub = b'/homeass'

def mqtt_event(topic, msg):
    print("New message on topic {}".format(topic.decode('utf-8')))
    msg = msg.decode('utf-8')
    print(msg)

def mqtt_connect():
    client = MQTTClient(client_id=client_id, server=mqtt_server, port=mqtt_port, user="MQTTUser", password="MQTTUserPassword", keepalive=3600)
    client.set_callback(mqtt_event)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to MQTT Broker. Reconnecting...')
    time.sleep(5)
    reset()
    
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
    

client.subscribe(topic_sub)

while True:
    try:
        print("waiting for message...")
        client.wait_msg()
    except OSError as e:
        reconnect()