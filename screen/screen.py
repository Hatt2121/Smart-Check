import sys
import os
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd4in2 as e
from PIL import Image, ImageDraw,ImageFont
import RPi.GPIO as GPIO
from time import sleep

CHECKBOX_LENGTH = 50

class Screen(e.EPD):
    def __init__(self):
        e.EPD.__init__(self)
        self.arial = ImageFont.truetype("arial.ttf")
    
    def print_main(self, item_list):
        '''
        The main image has 3 checklist items displaying at one time.
        '''
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
            if(type(str) == type(i)):
                draw.rectangle((cushion_left,cushion_top,cushion_left+50,cushion_top+50), fill = e.GRAY1, outline=e.GRAY4)
                draw.text((cushion_left+75, cushion_top),i,font=self.arial, fill= e.GRAY4)
                cushion_top += 100
        self.display(self.getbuffer(Mainimage))
        
        def turn_in(self,item):
            TurninImage = Image.new('1', (e.EPD_WIDTH,e.EPD_HEIGHT), 255)
            draw = ImageDraw.Draw(TurninImage)
            draw.rectangle((cushion_left, 125, cushion_left+50, 175), fill = GRAY1, outline=GRAY4)
            draw.text((100,125),item,font=self.arial,fill = e.GRAY4)

            self.display(self.getbuffer(TurninImage))
            time.sleep(2)
            self.Clear()

            TurninImage = Image.new('1', (e.EPD_WIDTH,e.EPD_HEIGHT), 255)
            draw = ImageDraw.Draw(TurninImage)
            draw.rectangle((cushion_left, 125, cushion_left+50, 175), fill = GRAY1, outline=GRAY4)
            draw.text((100,125),item,font=self.arial,fill = e.GRAY4)
            draw.line((25,125,75,175), fill= GRAY4)
            self.display(self.getbuffer(TurninImage))
            time.sleep(2)
            self.Clear()

