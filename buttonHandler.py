from  machine import Pin
from time import sleep

btn = Pin(26, Pin.IN, Pin.PULL_UP)
led = Pin("LED", Pin.OUT)

def btn_handler(pin):
    print(pin)
    led.toggle()
    sleep(0.2)

btn.irq(trigger = Pin.IRQ_RISING, handler = btn_handler)

while True:
    if led.value==1:
        print('Yo')
    sleep(0.5)