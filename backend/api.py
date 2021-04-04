from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from _thread import start_new_thread, allocate_lock

import logger


app = FastAPI()
lock = allocate_lock()

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


@app.get("/")
def index():
    with lock:
        return logger.get_last_values()


def from_thread():
    while True:
        with lock:
            logger.poll()


start_new_thread(from_thread, ())

