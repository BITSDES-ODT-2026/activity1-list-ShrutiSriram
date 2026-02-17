#Shruti Sriram Week_7 list activity code
from machine import Pin
import time

led1 = Pin(27,Pin.OUT)
led2 = Pin(32,Pin.OUT)
led3 = Pin(23,Pin.OUT)
led4 = Pin(4,Pin.OUT)
my_t = 0.5
my_list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
while True:
    for i in my_list:
        #1st second
        led1.value(i[0])
        led2.value(i[1])
        led3.value(i[2])
        led4.value(i[3])
        time.sleep(my_t)st
