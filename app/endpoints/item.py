from fastapi import APIRouter, HTTPException, responses
from app.models import InventoryItem
from typing import List
import uuid
from app.database.postgres import get_items_from_database, insert_item_into_database, get_items_by_user

router = APIRouter()

@router.post("/get_items")
async def items_get_by_id(item_ids: List[str]) -> List[InventoryItem]:

    # request the items from the database
    items = await get_items_from_database(item_ids)

    # if no items found, return 404
    if not items:
        raise HTTPException(status_code=404, detail="Items not found")

    # if found, return the items
    return items

@router.post("/get_items_by_user")
async def items_get_by_user(user_name: str) -> List[InventoryItem]:

    # request the items from the database
    items = await get_items_by_user(user_name)

    # if no items found, return 404
    if not items:
        raise HTTPException(status_code=404, detail="Items not found")

    # if found, return the items
    return items


@router.post("/insert_item")
async def item_post(item: InventoryItem) -> responses.Response:
    await insert_item_into_database(item)
    return responses.Response(status_code=200)