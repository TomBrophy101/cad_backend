from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

# FIXED: Re-added id here so FastAPI captures it from your new CSV format


class ItemCreate(ItemBase):
    id: int


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
