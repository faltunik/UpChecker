from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from repositories.checks import get_all_checks, get_checks, create_checks
from schemas.checks import CheckInSchema, CheckOutSchema


async def get_all_checks_service(
    db: Session,
    limit: int = 15, offset: int = 0
) -> List[CheckOutSchema]:
    checks = await get_all_checks(db=db, limit=limit, offset=offset)
    return [CheckOutSchema.from_orm(i) for i in checks]


async def get_checks_service(
        checks_id: int,
        db: Session) -> CheckOutSchema:
    check = await get_checks(checks_id=checks_id, db=db)
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Check not found")
    # return check : why we are not doing this?
    return CheckOutSchema(
        id=check.id,
        result=check.result,
        processed_at=check.processed_at,
        category_id=check.category_id,
        category=check.category
    )


async def create_checks_service(db: Session, check: CheckInSchema) -> CheckOutSchema:
    # wtf .from_orm does?
    return CheckOutSchema.from_orm(await create_checks(db=db, check=check))
