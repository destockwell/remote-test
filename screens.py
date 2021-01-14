#!/usr/bin/python3
#Frequency One Remote Screens
import time
#import subprocess
import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.ili9341 as ili9341
from PIL import Image, ImageDraw, ImageFont

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

class screen:
    cs_pin=None
    dc_pin=None
    rst_pin=None
    
    spi=None
    disp=None
    
    height=None
    width=None
    
    def __init__(self):
        # Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
        cs_pin = digitalio.DigitalInOut(board.CE0)
        dc_pin = digitalio.DigitalInOut(board.D25)
        rst_pin = digitalio.DigitalInOut(board.D24)

        # Setup SPI bus using hardware SPI:
        spi = board.SPI()

        # Create the ILI9341-based display, used by the 2.8 inch display and touchscreen:
        disp = ili9341.ILI9341(
            spi,
            rotation=270,
            cs=cs_pin,
            dc=dc_pin,
            rst=rst_pin,
            baudrate=BAUDRATE
        )

        # swap height/width to rotate it to landscape!

        if disp.rotation %180 == 90:
            height = disp.width
            width = disp.height
        else:
            height = disp.height
            width = disp.width

        # Define constants to allow easy resizing of shapes.
        # padding = -2
        # top = padding
        # bottom = height - padding
        # Move left to right keeping track of the current x position for drawing shapes.
        # x = 0

    def splash(self):
        # Turn on the backlight
        backlight = digitalio.DigitalInOut(board.D22)
        backlight.switch_to_output()
        backlight.value = True

        # Create blank image for drawing, and drawing object
        # Make sure to create image with mode 'RGB' for full color.

        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Load a TTF font.
        # fontfile="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=18)
        # font2 = ImageFont.truetype(fontfile, size=30)
        # font3 = ImageFont.truetype(fontfile, size=12)

        # Write splash screen text.
        draw.text((width/2, height/2-17), "Connecting to your", font=font1, align='center', fill=(0,0,128))
        draw.text((width/2, height/2), "FrequencyOne", font=font1.size=30, align='center', fill=(128,128,255))
        draw.text((width/2, height/2+17), "personal music channel", font=font1.size=12, align='center', fill=(0,0,128))

    # Display image: slow fade-in from dark blue to white, then fade out.
        disp.image(image, rotation)
        time.sleep(10.0)
