from decimal import Decimal
from typing import Annotated, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    username: str
    email: str
    password: str

# FIXED: Re-added id here so FastAPI captures it from your new CSV format


class ItemCreate(ItemBase):
    id: int


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
