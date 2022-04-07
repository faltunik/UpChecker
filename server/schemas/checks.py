from datetime import datetime

from pydantic import BaseModel

from .categories import CategoryOutSchema


class IdMixIn(BaseModel):
    id: int


class CheckBase(BaseModel):
    result: bool


class CheckInSchema(CheckBase):
    category_id: int


class CheckOutSchema(IdMixIn, CheckBase):
    processed_at: datetime
    
    category: CategoryOutSchema

    class Config:
        orm_mode = True
