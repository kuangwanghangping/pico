from machine import Pin
led = Pin(1,Pin.OUT)
while True:
    led.value(1)