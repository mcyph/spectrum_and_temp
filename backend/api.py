from asyncio import Queue, get_event_loop
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from _thread import start_new_thread, allocate_lock, get_ident

import logger


app = FastAPI()
lock = allocate_lock()
queues = {}

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/last_values")
def last_values():
    with lock:
        return logger.get_last_values()


@app.websocket("/last_values_ws")
async def websocket_endpoint(websocket: WebSocket):
    q = queues[get_ident()] = Queue()
    try:
        print("ACCEPTING WEBSOCKET..")
        await websocket.accept()
        print("WEBSOCKET ACCEPTED - SENDING TIME SERIES!")
        await websocket.send_json(logger.get_time_series())

        while True:
            print("GETTING FROM QUEUE...")
            await q.get()
            print("SENDING TO SOCKET")
            await websocket.send_json(logger.get_last_values())
    finally:
        del queues[get_ident()]


async def from_thread():
    # Poll from sensors
    while True:
        logger.poll()
        for id, q in queues.items():
            # Tell each websocket to update listeners
            await q.put(None)


get_event_loop().create_task(from_thread())
