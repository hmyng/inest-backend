from fastapi import FastAPI
from fastapi import APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.server.routes.data import router as DataRouter 

app = FastAPI()

consumer = None # define global consumer 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(DataRouter, tags=["data"], prefix="/data")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
