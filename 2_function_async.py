"""

Author: SquirtleSquadLeader

Purpose: Execute 2 seperate functions at given time intervals untilizing async.
         Replace the codes within function_1 and function_2 as desired to 
         repurpose this.  For example, blink an LED or transmit some data via 
         UART.  

"""

# Imports
import asyncio
from adafruit_ticks import ticks_ms, ticks_add, ticks_less, ticks_diff

async def function_1():
    print('Execturing function_1')
    await asyncio.core.sleep(0)
    
async def function_2(led):
    print('Execturing function_2')
    await asyncio.core.sleep(0)

async def main():

    # Desired time delays in milliseconds
    delay_1 = 1000
    delay_2 = 100
    
    # Set start of frame
    start_function_1 = ticks_ms()
    start_function_2 = ticks_ms()    
        
    while True:    
        
        if ticks_diff(ticks_ms(), start_function_1 ) > delay_1:
            start_function_1 = ticks_ms()
            asyncio.core.create_task(function_1())
            
        if ticks_diff(ticks_ms(), start_function_2) > delay_2:
            start_function_2 = ticks_ms()
            asyncio.core.create_task(function_2())
        
        await asyncio.core.sleep(0)
        
asyncio.core.run(main(led)) 
