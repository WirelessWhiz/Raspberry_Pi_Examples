import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  
pwm.start(0)

try:
    while True:
        
        pwm.ChangeDutyCycle(2.5)  
        time.sleep(1)  
        pwm.ChangeDutyCycle(7.5)  
        time.sleep(1) 
        pwm.ChangeDutyCycle(12.5) 
        time.sleep(1) 

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
