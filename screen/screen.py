import epd4in2 as e
from PIL import Image
import RPi.GPIO as GPIO


class Screen(e.EPD):
    def __init__(self):
        e.EPD.__init__(self)