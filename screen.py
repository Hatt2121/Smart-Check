import sys
import os
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd4in2 as epd
from PIL import Image, ImageDraw,ImageFont
import RPi.GPIO as GPIO
from time import sleep

arial = ImageFont.truetype("arial.ttf", 25)

def print_main(item_list):
        screen = epd.EPD()
        screen.init()
        items = []
        for i in range(3):
            try:
                items.append(item_list[i])
            except IndexError:
                items.append(NULL)
            continue

        Mainimage = Image.new('1', (epd.EPD_WIDTH,epd.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(Mainimage)
        cushion_left = 25
        cushion_top = 25
        for i in items:
            draw.rectangle((cushion_left,cushion_top,cushion_left+50,cushion_top+50), fill = epd.GRAY1, outline=epd.GRAY4)
            draw.text((cushion_left+75, cushion_top),i,font=arial, fill= epd.GRAY4)
            cushion_top += 100
        
        screen.display(screen.getbuffer(Mainimage))
        screen.Clear()
        screen.exit()

def turn_in(item):
    screen = epd.EPD()
    screen.init()

    cushion_left = 25
    cushion_top = 25
    TurninImage = Image.new('1', (epd.EPD_WIDTH,epd.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(TurninImage)
    draw.rectangle((cushion_left, 125, cushion_left+50, 175), fill = epd.GRAY1, outline= epd.GRAY4)
    draw.text((100,125),item,font=arial,fill = epd.GRAY4)
    
    screen.display(screen.getbuffer(TurninImage))
    sleep(2)
    screen.Clear()

    TurninImage = Image.new('1', (epd.EPD_WIDTH,epd.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(TurninImage)
    draw.rectangle((cushion_left, 125, cushion_left+50, 175), fill = epd.GRAY1, outline= epd.GRAY4)
    draw.text((100,125),item,font=arial,fill = epd.GRAY4)
    draw.line((25,125,75,175), fill= epd.GRAY4)
    screen.display(screen.getbuffer(TurninImage))
    sleep(2)
    screen.Clear()

#CHECKBOX_LENGTH = 50
''' OLD CODE!!!
class Screen(e.EPD):
    '''''''
    After you construct the object, make sure you do {Object}.init() this 
    function initializes the screen.
    ''''''
    def __init__(self):
        e.EPD.__init__(self)
        self.arial = ImageFont.truetype("arial.ttf", 25)
    
    def print_main(self, item_list):
        ''''''
        The main image has 3 checklist items displaying at one time.
        ''''''
        items = []
        for i in range(3):
            try:
                items.append(item_list[i])
            except IndexError:
                items.append(NULL)
            continue

        Mainimage = Image.new('1', (e.EPD_WIDTH,e.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(Mainimage)
        cushion_left = 25
        cushion_top = 25
        for i in items:
            draw.rectangle((cushion_left,cushion_top,cushion_left+50,cushion_top+50), fill = e.GRAY1, outline=e.GRAY4)
            draw.text((cushion_left+75, cushion_top),i,font=self.arial, fill= e.GRAY4)
            cushion_top += 100
        
        self.display(self.getbuffer(Mainimage))
        self.Clear()
        self.sleep()

    def turn_in(self,item):
        cushion_left = 25
        cushion_top = 25
        TurninImage = Image.new('1', (e.EPD_WIDTH,e.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(TurninImage)
        draw.rectangle((cushion_left, 125, cushion_left+50, 175), fill = e.GRAY1, outline= e.GRAY4)
        draw.text((100,125),item,font=self.arial,fill = e.GRAY4)

        self.display(self.getbuffer(TurninImage))
        sleep(2)
        self.Clear()

        TurninImage = Image.new('1', (e.EPD_WIDTH,e.EPD_HEIGHT), 255)
        draw = ImageDraw.Draw(TurninImage)
        draw.rectangle((cushion_left, 125, cushion_left+50, 175), fill = e.GRAY1, outline= e.GRAY4)
        draw.text((100,125),item,font=self.arial,fill = e.GRAY4)
        draw.line((25,125,75,175), fill= e.GRAY4)
        self.display(self.getbuffer(TurninImage))
        sleep(2)
        self.Clear()
'''