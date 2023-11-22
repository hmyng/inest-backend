from fastapi import APIRouter, status
from datetime import datetime

from server.dms.data import get_data

router = APIRouter()

@router.get('/', response_description="Get data")
async def getData(per_page: int=10, page: int=1, from_date: str='2021-01-01', to_date: str='2024-12-31'):
   data = await get_data(per_page, page, from_date, to_date)
   return data