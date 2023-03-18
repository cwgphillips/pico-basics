from  machine import Pin
import utime

pins = [
    Pin(15, Pin.OUT), #in1
    Pin(14, Pin.OUT), #in2
    Pin(16, Pin.OUT), #in3
    Pin(17, Pin.OUT), #in4
]

full_step_seqeuence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

while True:
    for step in  full_step_seqeuence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(0.001)