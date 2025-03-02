from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.websites import WebSiteInSchema, WebSiteOutSchema, WebSiteOutShortSchema, WebSiteUpdateSchema
from schemas.categories import CategoryOutSchema
from repositories.websites import create_website, delete_website, get_all_websites, get_website, update_website
from exceptions import NotFound


async def get_all_websites_service(
    db: Session,
    limit: int = 15, offset: int = 0
) -> List[WebSiteOutShortSchema]:
    websites = await get_all_websites(db=db, limit=limit, offset=offset)
    return [WebSiteOutShortSchema.from_orm(i) for i in websites]


async def get_website_service(db: Session, website_id: int) -> CategoryOutSchema:
    website = await get_website(db=db, website_id=website_id)
    if website is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Website not found")

    return WebSiteOutSchema(
        id=website.id,
        name=website.name,
        url=website.url,
        is_paused=website.is_paused,
        categories=website.categories.all()
    )


async def create_website_service(db: Session, website: WebSiteInSchema) -> WebSiteOutShortSchema:
    return WebSiteOutShortSchema.from_orm(await create_website(db=db, website=website))


async def update_website_service(db: Session, website_id: int, website: WebSiteUpdateSchema) -> WebSiteOutShortSchema:
    try:
        return WebSiteOutShortSchema.from_orm(await update_website(db=db, website_id=website_id, website=website))
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given website not found"
        )


async def delete_website_service(db: Session, website_id: int):
    try:
        await delete_website(db=db, website_id=website_id)
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given website not found"
        )
