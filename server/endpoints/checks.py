from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependices import get_db
from schemas.checks import CheckInSchema, CheckOutSchema
from services.checks import get_all_checks_by_category_id_service, get_check_service, create_checks_service


checks_endpoint = APIRouter(tags=["Checks"])


@checks_endpoint.get("/", response_model=List[CheckOutSchema])
async def get_all_checks_by_category_id_endpoint(category_id: int, db: Session = Depends(get_db), limit: int = 15, offset: int = 0) -> List[CheckOutSchema]:
    return await get_all_checks_by_category_id_service(category_id= category_id, db=db, limit=limit, offset=offset)


@checks_endpoint.get("/{check_id}", response_model=CheckOutSchema)
async def get_check_endpoint(
     check_id: int,
    db: Session = Depends(get_db)
) -> CheckOutSchema:
    return await get_check_service( check_id= check_id, db=db)


@checks_endpoint.post("/", response_model=CheckOutSchema, status_code=status.HTTP_201_CREATED)
async def create_checks_endpoint(check: CheckInSchema, db: Session = Depends(get_db)) -> CheckOutSchema:
    return await create_checks_service(db=db, check=check)
