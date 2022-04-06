from datetime import datetime

from pydantic import BaseModel

from .categories import CategoryOutSchema


class IdMixIn(BaseModel):
    id: int


class CheckBase(BaseModel):
    result: bool
    category_id: int


class CheckInSchema(CheckBase):
    pass


class CheckOutSchema(IdMixIn, CheckBase):
    processed_at: datetime
    
    category: CategoryOutSchema

    class Config:
        orm_mode = True
