#!/usr/bin/env python3
import aiy.audio
from aiy.audio import say
import aiy.voicehat
from time import sleep
import FaBo9Axis_MPU9250 as DOF

# this prgram was tested using the HC-SR501 Motion Detector
# That is is white one with a dome
# the code is set up to use the pins for Servo #5 on the hat


# this program uses an external proximity sensor to trigger a vocal alarm
def main():
    dof = DOF.MPU9250()

    print("Dont rock the boat baby!")
    say("Dont rock the boat baby!")
    sleep(1)

    boat_rocked = 0
    sens = -0.2
    while True:
        a = dof.readAccel()
        g = dof.readGyro()
        m = dof.readMagnet()
        print("accel: ", a)
        print("gyro : ",g)
        print("mag  : ", m)
        if a['x'] < sens or a['y'] < sens or a['z'] < sens:
            print("dont rock the boat!")
            say("Hey dont rock the boat!")
            boat_rocked = boat_rocked + 1;
            if boat_rocked % 4 == 3:
                print("BABY!")
                say("BABY!")
        print("---------------------")
        sleep(0.25)


if __name__ == "__main__":
    main()
