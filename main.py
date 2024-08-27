from machine import Pin,SPI,PWM
import framebuf
import utime
import time
import os
import math
import random
from System.Drivers.LCD import lcd
from System.system import System as Sstm


# =================== Main ======================

'''
# Set up buttons & joystick
keyA = Pin(15,Pin.IN,Pin.PULL_UP)

keyX = Pin(19 ,Pin.IN,Pin.PULL_UP)
keyY= Pin(21 ,Pin.IN,Pin.PULL_UP)

up = Pin(2,Pin.IN,Pin.PULL_UP)
down = Pin(18,Pin.IN,Pin.PULL_UP)
left = Pin(16,Pin.IN,Pin.PULL_UP)
right = Pin(20,Pin.IN,Pin.PULL_UP)
ctrl = Pin(3,Pin.IN,Pin.PULL_UP)
if keyA.value() == 0: print("A Pressed")
'''

LED = Pin(25, Pin.OUT)
keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)
keyX = Pin(19,Pin.IN,Pin.PULL_UP)
keyY = Pin(21,Pin.IN,Pin.PULL_UP)
up = Pin(2,Pin.IN,Pin.PULL_UP)
down = Pin(18,Pin.IN,Pin.PULL_UP)
left = Pin(16,Pin.IN,Pin.PULL_UP)
right = Pin(20,Pin.IN,Pin.PULL_UP)
ctrl = Pin(3,Pin.IN,Pin.PULL_UP)
# Set up button A - INPUT

# ========== Start of crib code ==============
# simple text (s,x,y,c)
lcd.show()


    
Sstm(lcd, keyA, keyB, keyX, keyY, up, down, right, left, ctrl)