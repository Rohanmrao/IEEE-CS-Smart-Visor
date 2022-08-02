# this is the relay implemtation
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
relay = 17
GPIO.setup(relay, GPIO.OUT) # GPIO Assign mode
while(True):
    GPIO.output(relay, GPIO.LOW) # out
    sleep(3)
    GPIO.output(relay, GPIO.HIGH) # on
    sleep(3)
    
GPIO.cleanup()
