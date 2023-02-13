# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
"""NeoKey simpletest."""
import board
import busio
from adafruit_neokey.neokey1x4 import NeoKey1x4

# use default I2C bus
i2c_bus = busio.I2C(board.SCL1, board.SDA1)

# Create a NeoKey object
neokey = NeoKey1x4(i2c_bus, addr=0x31)

keys_state = [False, False, False, False];
print("Adafruit NeoKey simple test")

# Check each button, if pressed, light up the matching neopixel!
while True:
    if neokey[0]:
        if not keys_state[0]:
            print("")
            neokey.pixels[0] = 0xFF0000
            keys_state[0] = True
    else:
        neokey.pixels[0] = 0x0
        keys_state[0] = False

    if neokey[1]:
        if not keys_state[1]:
            print("")
            keys_state[1] = True
            neokey.pixels[1] = 0xFFFF00
    else:
        neokey.pixels[1] = 0x0
        keys_state[1] = False

    if neokey[2]:
        if not keys_state[2]:
            print("")
            neokey.pixels[2] = 0x00FF00
            keys_state[2] = True
    else:
        neokey.pixels[2] = 0x0
        keys_state[2] = False

    if neokey[3]:
        if not keys_state[3]:
            print("")
            neokey.pixels[3] = 0x00FFFF
            keys_state[3] = True
    else:
        neokey.pixels[3] = 0x0
        keys_state[3] = False
