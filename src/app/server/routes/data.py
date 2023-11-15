from fastapi import APIRouter, status
from datetime import datetime

from server.dms.data import get_data

router = APIRouter()

@router.get('/', response_description="Get data")
async def getData():
   data = await get_data()
   return data