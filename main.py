import asyncio
import random
import time
x = ["1", "2", "nyhha", "3", "4hgas", "5dasdas"]

from websockets.server import serve

async def echo(websocket):
    while True:
        l = random.choice(x)
        await websocket.send(l)
        time.sleep(1)

async def main():
    async with serve(echo, "0.0.0.0", 8000):
        await asyncio.Future()  # run forever

asyncio.run(main())