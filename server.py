import asyncio
from store_data import save_ecg
from fastapi import FastAPI, WebSocket

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    print("Client connected")

    clients.append(websocket)

    try:
        while True:

            data = await websocket.receive_text()

            for client in clients:
                try:
                    await client.send_text(data)
                except:
                    pass

    except Exception as e:
        print("Connection closed:", e)

    finally:
        clients.remove(websocket)