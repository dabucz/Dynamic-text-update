import asyncio
import websockets
import random
import time
x = ["1", "2", "", "3", "4", "5"]
async def handle_connection(websocket, path):
    while True:
        l = random.choice(x)
        print(l)
        await websocket.send(l)
        time.sleep(1)
async def start_server():
    async with websockets.serve(handle_connection, "localhost", 8000):
        print("WebSocket server started")
        await asyncio.Future()

asyncio.run(start_server())
