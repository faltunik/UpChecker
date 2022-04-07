from typing import List

from sqlalchemy.orm import Session

from models import Check
from schemas.checks import CheckInSchema


async def get_all_checks_by_category_id(
    db: Session,
    category_id: int,
    limit: int = 15, offset: int = 0
) -> List[Check]:
    return db.query(Check).filter(category_id= category_id).limit(limit).offset(offset).all()


async def get_check_by_category_id( check_id: int, db: Session) -> Check:
    return db.query(Check).get( check_id)
    # why we are not using?: db.query(models.Post).filter(models.Post.id == post_id).first()


async def create_check_by_category_ids(db: Session, check: CheckInSchema) -> Check:
    created_check = Check(
        **check.dict()
    )
    db.add(created_check)
    db.commit()
    db.refresh(created_check)
    return created_check
