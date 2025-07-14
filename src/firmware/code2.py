import time
import board
import math
import busio
import terminalio
import displayio
from adafruit_display_text import label
import gc9a01

# Release any resources currently in use for the displays
displayio.release_displays()

# Raspberry Pi Pico pinout, one possibility, at "southwest" of board
tft_clk = board.GP10 # must be a SPI CLK
tft_mosi= board.GP11 # must be a SPI TX
tft_rst = board.GP12
tft_dc  = board.GP13
tft_cs  = None
tft_bl  = None
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)


# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

# Make the main display context
main = displayio.Group()
display.root_group = main

# Draw a text label
text = "Hello\nWorld!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00,
                        anchor_point=(0.5,0.5), anchored_position=(0,0))
text_group = displayio.Group(scale=2)
text_group.append(text_area) 
main.append(text_group)

# Animate the text 
theta = math.pi
r = 75
while True:
    print(time.monotonic(),"hello")
    text_group.x = 120 + int(r * math.sin(theta))
    text_group.y = 120 + int(r * math.cos(theta))
    theta -= 0.05
    time.sleep(0.01)