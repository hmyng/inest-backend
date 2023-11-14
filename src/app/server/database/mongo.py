import os
from pymongo import MongoClient
import motor.motor_asyncio
from decouple import config

MONGO_URI = config("MONGO_URI")
MONGO_DB = config("MONGO_DB")
client = MongoClient(MONGO_URI)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.get_database(MONGO_DB)
data_collection = database.get_collection("data")

