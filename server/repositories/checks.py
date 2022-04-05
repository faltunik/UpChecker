from typing import List
from models import Check
from sqlalchemy.orm import Session
from schemas.checks import CheckInSchema


async def get_all_checks(
    db: Session,
    limit: int = 15, offset: int = 0
) -> List[Check]:
    return db.query(Check).limit(limit).offset(offset).all()

async def get_checks(checks_id: int, db: Session) -> Check:
    return db.query(Check).get(checks_id)
    # why we are not using?: db.query(models.Post).filter(models.Post.id == post_id).first()

async def create_checks(db: Session, check: CheckInSchema) -> Check:
    # created_check = Check(
    #     result = check.result,
    #     category = check.category_id,
    # )
    created_check = Check(
        **check.dict()
    )
    db.add(created_check)
    db.commit()
    db.refresh(created_check)
    return created_check
