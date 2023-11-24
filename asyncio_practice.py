"""

Author: SquirtleSquadLeader

Hardware: Adafruit M4 Feather Can Express

Purpose: Loop 2 seperate functions utilizing asyncio.   

"""

# Imports
import board
import asyncio
import digitalio
from adafruit_ticks import ticks_ms, ticks_add, ticks_less, ticks_diff

# Configure LED pin
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

async def function_1():
    print('Execturing function_1')
    await asyncio.core.sleep(0)
    
async def function_2(led):
    print('Execturing function_2')
    led.value = not led.value
    await asyncio.core.sleep(0)

async def main(led):
    # Set start of frame
    start_function_1 = ticks_ms()
    start_function_2 = ticks_ms()    
        
    while True:    
        if ticks_diff(ticks_ms(), start_print ) > 1000:
            start_print = ticks_ms()
            asyncio.core.create_task(function_1())
            
        if ticks_diff(ticks_ms(), start_function_2) > 100:
            start_function_2 = ticks_ms()
            asyncio.core.create_task(function_2(led))
        
        await asyncio.core.sleep(0)
        
asyncio.core.run(main(led))   
