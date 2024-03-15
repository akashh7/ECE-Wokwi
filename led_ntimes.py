#to blink n  number of times
from machine import Pin
from time import sleep 
led3 = Pin(5, Pin.OUT)
counter = int(input("Enter counter: "))
i = 1;
while (i<=counter):
    led3.on()
    print("On")
    sleep(1)
    led3.off()
    print("Off")
    sleep(1)
    i = i+1

