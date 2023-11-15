import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Data(BaseModel):
    time: str = Field(...)
    CH3: str = Field(...)
    CH4: str = Field(...)