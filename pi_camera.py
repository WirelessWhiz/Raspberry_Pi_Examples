from picamera import PiCamera
import time

camera = PiCamera()
try:
    while True:
        camera.capture('/home/pi/image.jpg')
        print("Image captured")
        time.sleep(5)

except KeyboardInterrupt:
    camera.close()
