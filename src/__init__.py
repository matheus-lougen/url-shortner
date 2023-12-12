import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.routes import router

static_folder = f'{os.path.dirname(os.path.realpath(__file__))}/static'
app = FastAPI(title='app')
app.mount("/static", StaticFiles(directory=static_folder), name='static')
app.include_router(router)
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
