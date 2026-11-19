from decimal import Decimal
from typing import Annotated, Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    # FIXED: Added price field to match the model
    price: Annotated[Decimal, Field(gt=0, max_digits=10, decimal_places=2)]

# FIXED: Re-added id here so FastAPI captures it from your new CSV format


class ItemCreate(ItemBase):
    id: int


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
