"""

Author: SquirtleSquadLeader

Hardware: Adafruit M4 Feather Can Express

Loop 2 seperate functions utilizing asyncio.  My intent is to replace these functions with more complex logic.  

"""


# Imports
import board
import asyncio
import digitalio
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
        
    while True:    
        if ticks_diff(ticks_ms(), start_print ) > 1000:
            start_print = ticks_ms()
            asyncio.core.create_task(print_stuff())
            
        if ticks_diff(ticks_ms(), start_blink) > 100:
            start_blink = ticks_ms()
            asyncio.core.create_task(blink(led))
        
        await asyncio.core.sleep(0)
        
asyncio.core.run(main(led))   
    
