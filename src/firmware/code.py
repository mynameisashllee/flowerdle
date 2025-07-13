import board
import digitalio
import analogio
import time
import random
import math
import busio
import terminalio
import displayio
from adafruit_display_text import label
import gc9a01 # type: ignore
from vectorio import Rectangle

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

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst) # type: ignore
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

# Make the main display context
main = displayio.Group()
display.root_group = main



# Draw a text label
palette = displayio.Palette(1)
palette[0] = 0xffffff
bar_group = displayio.Group(scale=2)
bar = Rectangle(pixel_shader=palette, x=60, y=0, width=5, height=240)
bar_group.append(bar)
main.append(bar_group)
p1_status = displayio.Group(scale=2)
p2_status = displayio.Group(scale=2)
palette_win = displayio.Palette(1)
palette_win[0] = 0x00ff00
p1_color = Rectangle(pixel_shader=palette_win, x=0, y=0, width=120, height=240)
p2_color = Rectangle(pixel_shader=palette_win, x=60, y=0, width=120, height=240)
p1_status.append(p1_color)
p2_status.append(p2_color)

p1, p2 = 5, 5
p1_text = str(p1)
p1_text_area = label.Label(terminalio.FONT, text=p1_text, color=0xFFFF00,
                        anchor_point=(3.5,3.5), anchored_position=(30,60))
p1_text_group = displayio.Group(scale=5)
p1_text_group.append(p1_text_area) 
main.append(p1_text_group)
p2_text = str(p2)
p2_text_area = label.Label(terminalio.FONT, text=p2_text, color=0xFFFF00,
                        anchor_point=(3.5,3.5), anchored_position=(55,60))
p2_text_group = displayio.Group(scale=5)
p2_text_group.append(p2_text_area) 
main.append(p2_text_group)

wrong_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7]
right_pins = [board.GP14, board.GP15, board.GP16, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22]
analog_pins = [board.GP26, board.GP27, board.GP28, board.GP28]

wrongs: list[digitalio.DigitalInOut] = []
rights: list[digitalio.DigitalInOut] = []
analog: list[analogio.AnalogIn] = []
for i in wrong_pins:
    wrongs.append(digitalio.DigitalInOut(i))
    wrongs[-1].direction = digitalio.Direction.OUTPUT
for i in right_pins:
    rights.append(digitalio.DigitalInOut(i))
    rights[-1].direction = digitalio.Direction.OUTPUT
for i in analog_pins:
    analog.append(analogio.AnalogIn(i))

mp = {
    48: 0,
    47: 0,
    46: 0,
    36: 1,
    35: 1,
    34: 1,
    23: 2,
    22: 2,
    21: 2,
    13: 3,
    12: 3,
    11: 3
}

def read(sw1:  digitalio.DigitalInOut, sw2:  digitalio.DigitalInOut, sw3:  digitalio.DigitalInOut, sw4:  digitalio.DigitalInOut):
    tmp1, tmp2, tmp3, tmp4 = sw1.value, sw2.value, sw3.value, sw4.value
    p1, p2 = [], []
    sw1.value, sw2.value, sw3.value, sw4.value = True, False, False, False # p1 main
    p1.append(analog[0].value)
    p1.append(analog[1].value)
    p1.append(analog[2].value)
    sw1.value, sw2.value, sw3.value, sw4.value = False, True, False, False # p1 sub
    p1.append(analog[2].value)
    sw1.value, sw2.value, sw3.value, sw4.value = False, False, True, False # p2 main
    p2.append(analog[0].value)
    p2.append(analog[1].value)
    p2.append(analog[2].value)
    sw1.value, sw2.value, sw3.value, sw4.value = False, False, False, True # p2 sub
    p2.append(analog[2].value)
    sw1.value, sw2.value, sw3.value, sw4.value = tmp1, tmp2, tmp3, tmp4
    return p1, p2

    

ans = [0, 1, 2, 3]
random.shuffle(ans)

p1_lock, p2_lock = False, False
while True:
    p1, p2 = read(wrongs[0], wrongs[1], wrongs[4], wrongs[5])
    if all([x // 1000 > 0 for x in p1]) and not p1_lock:
        p1_lock = True
        for i in range(4):
            wrongs[i].value = not(mp[p1[i] // 1000] == ans[i])
            rights[i].value = mp[p1[i] // 1000] == ans[i]
    elif all([x // 1000 < 0 for x in p1]) and p1_lock:
        p1_lock = False

    if all([x // 1000 > 0 for x in p2]) and not p2_lock:
        p2_lock = True
        for i in range(4):
            wrongs[i].value = not(mp[p2[i] // 1000] == ans[i])
            rights[i].value = mp[p2[i] // 1000] == ans[i]
    elif all([x // 1000 < 0 for x in p2]) and p2_lock:
        p2_lock = False
    time.sleep(0.5)

# 1.2k = 47***
# 2k   = 35***
# 3.4k = 22***
# 4.2k = 12***