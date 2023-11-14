from fastapi import APIRouter, status
from datetime import datetime

router = APIRouter()

@router.get('/', response_description="Get data")
async def getData():
   return []