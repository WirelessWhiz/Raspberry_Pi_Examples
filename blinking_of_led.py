import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH) 
        time.sleep(1) 
        GPIO.output(led_pin, GPIO.LOW)  
        time.sleep(1) 
except KeyboardInterrupt:
    GPIO.cleanup()