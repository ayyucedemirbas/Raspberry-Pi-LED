import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,0)
GPIO.output(18,1)
time.sleep(10)
GPIO.cleanup()