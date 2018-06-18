#!/usr/bin/python3
from gpiozero import PWMOutputDevice as PWM
from time import sleep

motors = [PWM(4), PWM(17), PWM(27), PWM(22)]

while True:
    print("motor on")
    motors[0].on()
    sleep(1)
    print("motor off")
    motors[0].off()
    sleep(1)
    print("motor 50%")
    motors[0].value = 0.5
    sleep(2)
    print("motor 20%")
    motors[0].value = 0.2
    sleep(2)
