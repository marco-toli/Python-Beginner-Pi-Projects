from picamera import PiCamera
from time import sleep
import datetime
import RPi.GPIO as GPIO
import sys, os

#import pigpio
#piLED = pigpio.pi()

#GPIO.setwarnings(False)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, GPIO.OUT)


#camera = PiCamera()
#setting camera resoolution to max
#camera.resolution = (2592, 1944)
#camera.framerate = 15

#camera.start_preview()
#for video
#sleep(2)
#camera.start_recording('./video/video.mov')
#sleep(10)
#camera.stop_recording()

#for snapshot
print "have you checked the picID ? (to avoid overwriting)"
sleep(5)
picID = 0
#GPIO.output(3, 0)
os.system("sudo service motion stop")

for i in range(1000000):
#for i in range(5):
#    sleep(60*60*6)
#    sleep(1)

    #each hour check what time is it
#    sleep(60*60 - 4)
    now = datetime.datetime.now()
    print "checking time... ", now

    #if during target hours
#    if (1):
#    if ((now.hour == 8 or now.hour == 9 or now.hour == 10 or now.hour == 11 or now.hour == 12 or now.hour == 13 or now.hour == 14 or now.hour == 15 or now.hour == 16 or now.hour == 17 or now.hour == 18 or now.hour == 19 or now.hour == 20 or now.hour == 21) and now.minute == 0):
    if ( (now.minute == 0 or now.minute == 30 or now.minute == 15 or now.minute == 45) and now.hour!=0 and now.hour!=1 and now.hour != 2 and now.hour != 3 and now.hour != 4 and now.hour !=5 and now.hour != 23):
        camera = PiCamera()
        #setting camera resoolution to max
        camera.resolution = (2592, 1944)
        camera.framerate = 15

        camera.start_preview()
#
        if (now.hour < 17 ):
            camera.brightness = 50
        else:
            camera.brightness = 45
#        camera.ISO = 200
#        os.system("sh switch_on_usb.sh")

        sleep(17) #tune the ISO
        camera.capture('/media/pi/Elements/time_lapse/image_%06d.jpg' % picID)
#        camera.capture('/media/pi/Elements/time_lapse/image_test.jpg')

        print "taking picture..."
#        sleep(60*60*6)
        picID+=1
        camera.stop_preview()
        sleep(1)
#        os.system("sh switch_off_usb.sh")
        camera.close()
        sleep(12)

    else:
        sleep(30)


    # wait for 30 s
    for j in range(3):
  #      GPIO.output(3, 1)
 #       print "looping on LED..."
      #  sleep(0.1)
 #       GPIO.output(3, 0)
        sleep(10)

#    os.system("sh switch_off_usb.sh")

#GPIO.cleanup()
