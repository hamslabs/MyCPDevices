# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
"""NeoKey simpletest."""
import board
import busio
from adafruit_neokey.neokey1x4 import NeoKey1x4
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode



# use default I2C bus
i2c_bus = busio.I2C(board.SCL1, board.SDA1)

# Create a NeoKey object
neokey = NeoKey1x4(i2c_bus, addr=0x30)

keys_state = [False, False, False, False];

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Check each button, if pressed, light up the matching neopixel!
while True:
    if neokey[0]:
        if not keys_state[0]:
            keyboard_layout.write("")
            neokey.pixels[0] = 0xFF0000
            keys_state[0] = True
    else:
        neokey.pixels[0] = 0x0
        keys_state[0] = False

    if neokey[1]:
        if not keys_state[1]:
            keyboard_layout.write("")
            keys_state[1] = True
            neokey.pixels[1] = 0xFFFF00
    else:
        neokey.pixels[1] = 0x0
        keys_state[1] = False

    if neokey[2]:
        if not keys_state[2]:
            keyboard_layout.write("")
            neokey.pixels[2] = 0x00FF00
            keys_state[2] = True
    else:
        neokey.pixels[2] = 0x0
        keys_state[2] = False

    if neokey[3]:
        if not keys_state[3]:
            keyboard_layout.write("")
            neokey.pixels[3] = 0x00FFFF
            keys_state[3] = True
    else:
        neokey.pixels[3] = 0x0
        keys_state[3] = False
