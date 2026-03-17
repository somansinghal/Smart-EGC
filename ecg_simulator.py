import asyncio
import math
import websockets

async def stream_ecg():

    uri = "ws://127.0.0.1:8000/ws"

    print("Connecting to server...")

    async with websockets.connect(uri) as websocket:

        print("Connected!")

        t = 0

        while True:

            value = 2048 + 400 * math.sin(2 * math.pi * 1.3 * t)

            await websocket.send(str(value))

            t += 0.01

            await asyncio.sleep(0.01)

asyncio.run(stream_ecg())