import RPi.GPIO as GPIO
import time

rel = 13
ldr = 15
ldr_val = 0 # init value

GPIO.setmode(GPIO.BOARD)
GPIO.setup(rel, GPIO.OUT)

GPIO.output(rel,GPIO.HIGH)

def rc_time(ldr):
        count = 0
        GPIO.setup(ldr,GPIO.OUT)
        GPIO.output(ldr,GPIO.LOW)
        time.sleep(0.1)
        cur_time = time.time()#getting the current time
        GPIO.setup(ldr,GPIO.IN)
        while(GPIO.input(ldr) == GPIO.LOW):
                count = time.time() - cur_time

        return (count*1000)
try:
        while True:

                ldr_val = int(rc_time(ldr))
                print(ldr_val)

                if(ldr_val > 3):
                        GPIO.output(rel,GPIO.HIGH)

                if(ldr_val <= 3):
                        GPIO.output(rel,GPIO.LOW)


except KeyboardInterrupt:
        GPIO.cleanup()

