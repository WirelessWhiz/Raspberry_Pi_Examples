from picamera import Picamera
import time

camera=Picamera
try:
    while True:
        camera.start_preview('/home/pi/image.jpg')
        time.sleep(5)
        camera.stop_preview('/home/pi/image.jpg')
except KeyboardInterrupt:
    camera.close()


