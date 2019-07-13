from picamera import PiCamera
from time import sleep
import sys, os

camera = PiCamera()
#setting camera resoolution to max
camera.resolution = (2592, 1944)
camera.framerate = 15

camera.start_preview()
#for video
sleep(2)
#camera.start_recording('./video/video.mov')
#sleep(10)
#camera.stop_recording()


#for snapshot
for i in range(1):
#    bright_level = 50
#    camera.brightness = bright_level
#    camera.exposure_mode = 'off'
    ISO_level = 100
#    camera.ISO = ISO_level
#    camera.shutter_speed = 200
    sleep(2)
    camera.capture('./pics/image_final_test%s.jpg' % ISO_level)
camera.stop_preview()
