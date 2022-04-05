from typing import Optional
from pydantic import AnyHttpUrl, BaseModel
from .categories import CategoryOutSchema
from datetime import datetime


class IdMixIn(BaseModel):
    id: int


class CheckBase(BaseModel):
    result: bool


class CheckInSchema(CheckBase):
    category_id: int


class CheckOutSchema(IdMixIn, CheckBase):
    processed_at: datetime
    category_id: int
    category: CategoryOutSchema

    class Config:
        orm_mode = True
