from machine import Pin
import time

led = Pin(16, Pin.OUT)
button = Pin(17, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.2)