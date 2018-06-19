#!/usr/bin/env python3
# This program is for interfacing with mpi9265 or other
# MPU9250 style 9-DOF sensors
# These sensors are connected to the Raspberry Pi Via the GND, 3V, SDA and SCL I2C lines

import aiy.audio
from aiy.audio import say
import aiy.voicehat
from time import sleep
import FaBo9Axis_MPU9250 as DOF

def main():

    dof = DOF.MPU9250()
    print("initializing MPU9265 9DOF Test")
    say("initializing M P U 92 65 9 D O F Test")
    sleep(1)

    while True:
        a = dof.readAccel()
        g = dof.readGyro()
        m = dof.readMagnet()
        print("accel: ", a)
        print("gyro : ",g)
        print("mag  : ", m)
        print("---------------------")
        sleep(0.25)

if __name__ == "__main__":
    main()
