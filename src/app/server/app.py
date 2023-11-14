import logging
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

# initialize logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_event():
    log.info('Shutting down kafka consumer')
    await consumer.stop()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
