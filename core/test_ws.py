import asyncio
import json
from asyncio import sleep

import websockets


async def hello():
    async with websockets.connect("ws://localhost:8000/ws/2/") as websocket:
        while True:
            # await websocket.send(json.dumps({"type": "test", "message": "Hello"}))
            data = await websocket.recv()
            await sleep(0.1)
            print(data)

asyncio.run(hello())
