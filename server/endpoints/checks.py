from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependices import get_db
from schemas.checks import CheckInSchema, CheckOutSchema
from services.checks import get_all_checks_service, get_checks_service, create_checks_service




checks_endpoint = APIRouter(tags=["Checks"])


# explain working of List
@checks_endpoint.get("/", response_model=List[CheckOutSchema])
async def get_all_checks_endpoint(db: Session = Depends(get_db), limit: int = 15, offset: int = 0) -> List[CheckOutSchema]:
    return await get_all_checks_service(db=db, limit=limit, offset=offset)


@checks_endpoint.get("/{checks_id}", response_model=CheckOutSchema)
async def get_checks_endpoint(
    checks_id: int,
    db: Session = Depends(get_db)
) -> CheckOutSchema:
    return await get_checks_service(checks_id=checks_id, db=db)


@checks_endpoint.post("/", response_model=CheckOutSchema, status_code=status.HTTP_201_CREATED)
async def create_checks_endpoint(check: CheckInSchema, db: Session = Depends(get_db)) -> CheckOutSchema:
    return await create_checks_service(db=db, check=check)
