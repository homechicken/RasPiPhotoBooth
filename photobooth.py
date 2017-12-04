#!/usr/bin/python

from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
from gpiozero import LED
from gpiozero import Button

led = LED(17)
button = Button(2)

camera = PiCamera()

camera.resolution = camera.MAX_RESOLUTION

# This block for simple camera test
#camera.start_preview(resolution=(1920,1080))
#sleep(3)
#camera.capture('ttt.jpg')

# This block for testing the LED
#while True:
#  led.on()
#  sleep(1)
#  led.off()
#  sleep(1)

# This block for switch test
#while True:
#  button.wait_for_press()
#  print('Button pressed')
#  sleep(1)

# function for taking pictures
def capture():
  camera.start_preview(resolution=(1920,1080))
#  camera.annotate_foreground = Color('yellow')
#  camera.annotate_text = "Chief Architect Christmas Party 2017"
#  camera.image_effect = 'cartoon'
  filename = datetime.now().isoformat()
  sleep(3)
  led.blink(0.1, 0.1)
  sleep(1)
  led.off()
  camera.capture('/home/pi/Pictures/%s.jpg' % filename)
  camera.stop_preview()
  sleep(2)

while True:
  button.wait_for_press()
  capture()
  

# This block for button and LED test
#button.when_pressed = led.on
#button.when_pressed = led.off

# This block for overlay text. No background = transparent
#camera.start_preview(resolution=(1920,1080))
#camera.annotate_background = Color('blue')
#camera.annotate_foreground = Color('yellow')
#camera.annotate_text = "Chief Architect Christmas Party 2017"
#sleep(5)
#camera.stop_preview()


# This block for camera image effects
#camera.image_effect = 'none'
# Effects are: none, negative, solarize*, sketch, denoise, emboss, oilpaint*,
#    gpen, pastel, watercolor*, film, blur, saturation, colorswap*, washedout,
#    posterise*, colorpoint, colorbalance, cartoon*, deinterlace1, deinterlace2

# This block for Chief Architect Christmas Party Photobooth 2017
#while True:
#  button.wait_for_press()
#  camera.start_preview(resolution=(1920,1080))
#  sleep(3)
#  led.blink(0.1, 0.1)
#  sleep(1)
#  led.off()
#  camera.capture('ttt.jpg')
#  sleep(2)


# This block for multiple sequential photos
#camera.start_preview()
#for i in range(5):
# sleep(5)
# camera.capture('image%s.jpg' % i)
#camera.stop_preview()


# This block loops through all effects
#camera.start_preview(resolution=(1920,1080))
#for effect in camera.IMAGE_EFFECTS:
# camera.image_effect = effect
# camera.annotate_text = "Effect: %s" % effect
# sleep(2)
#camera.stop_preview()
