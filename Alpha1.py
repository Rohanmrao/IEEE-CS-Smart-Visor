from gpiozero import LightSensor
from signal import pause
from gpiozero import LED
from gpiozero import AngularServo
from time import sleep


#defining all the pin values here 
ldr_pin_no = 18
servo1_pin = 17
servo2_pin = 16


#################################
sensor = LightSensor(ldr_pin_no) # sensor definition
servo1 = AngularServo(servo1_pin, min_angle = 0, max_angle = 90)
servo2 = AngularServo(servo2_pin, min_angle = 0, max_angle = 90) #definition of servos


def add_tint(s1,s2):
    s1.max()
    s2.max()

def remove_tint(s1,s2):
    s1.min()
    s2.min()

while True:
    sensor.when_light = add_tint(servo1,servo2)
    sensor.when_dark = remove_tint(servo1,servo2)

    pause()


    