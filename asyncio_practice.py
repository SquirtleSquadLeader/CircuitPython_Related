"""
M4 Feather Can Express
Ethernet Featherwing

"""

import time
import board
import neopixel
import asyncio
import digitalio
import rotaryio

from micropython import const
from adafruit_seesaw.seesaw import Seesaw
from adafruit_ticks import ticks_ms, ticks_add, ticks_less, ticks_diff

# Configure LED pin
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


async def print_stuff():
    print('test')
    await asyncio.core.sleep(0)
    
async def blink(led):
    led.value = not led.value
    await asyncio.core.sleep(0)

async def main(led):
    # Set start of frame
    start_blink = ticks_ms()
    start_print = ticks_ms()
    
    loop = asyncio.core.get_event_loop()
        
    while True:    
        if ticks_diff(ticks_ms(), start_print ) > 1000:
            start_print = ticks_ms()
            asyncio.core.create_task(print_stuff())
            
        if ticks_diff(ticks_ms(), start_blink) > 100:
            start_blink = ticks_ms()
            asyncio.core.create_task(blink(led))
        
        await asyncio.core.sleep(0)
        
asyncio.core.run(main(led))



        
"""
need to code:

    while one task is still alive.... generate another blink
"""
     
    
                                   
    

    
