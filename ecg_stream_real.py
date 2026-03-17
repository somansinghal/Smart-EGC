import asyncio
import wfdb
import websockets
import numpy as np

async def stream_ecg():

    # load ECG dataset
    record = wfdb.rdrecord('100', pn_dir='mitdb')
    signal = record.p_signal[:,0]

    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as websocket:

        for value in signal:

            # scale ECG value to ADC range
            value = (value + 1) * 2000

            await websocket.send(str(value))

            await asyncio.sleep(0.004)  # ~250Hz sampling

asyncio.run(stream_ecg())