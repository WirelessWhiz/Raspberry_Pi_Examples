from picamera import Picamera
import time

camera=Picamera()
try:
    while True:
        camera.start_recording('/home/pi/image.jpg')
        time.sleep(5)
        camera.stop_recording()
finally:
    camera.close()

