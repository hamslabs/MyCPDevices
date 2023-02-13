# SPDX-FileCopyrightText: Copyright (c) 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
International layout demo for MacroPad.
"""
import time
from adafruit_macropad import MacroPad

macropad = MacroPad()

keycodes = [
	# Row 1
    "",
    "",
    "",
	
	# Row 2
	"",
    "",
    "",

	# Row 3
    "",
    "",
    "",

	# Row 4
    "",
    "",
    "",
]

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        keycode = keycodes[key_event.key_number]
        if key_event.pressed:
            if isinstance(keycode, int):
                macropad.keyboard.press(keycode)
            else:
                macropad.keyboard_layout.write(keycode)
        else:
            if isinstance(keycode, int):
                macropad.keyboard.release(keycode)
    time.sleep(0.05)
