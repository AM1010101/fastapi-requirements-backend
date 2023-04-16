import asyncpg
from app.models import InventoryItem
from app.settings import Settings
from fastapi import HTTPException
from typing import List

settings = Settings()

async def get_items_from_database(item_ids: List[str]) -> List[InventoryItem]:
    # set up database connection
    print("connecting to database")
    conn = await asyncpg.connect(user=settings.POSTGRES_USER, password=settings.POSTGRES_PASSWORD,
                                  database=settings.POSTGRES_DB, host=settings.POSTGRES_HOST, port=settings.POSTGRES_PORT)

    # execute SQL query to retrieve items with matching UUIDs
    print("running query")
    query = 'SELECT * FROM inventoryitem WHERE id = ANY($1)'
    rows = await conn.fetch(query, item_ids)

    # close database connection
    await conn.close()

    # if no items found, return empty list
    if not rows:
        return []

    # create and return list of Item objects
    items = []
    for row in rows:
        item = InventoryItem(
            name=row['name'],
            price=row['price'],
            image=row['image'],
            description=row['description'],
            brand=row['brand'],
            currentInventory=row['currentinventory'],
            id=row['id'],
            user_name=row['user_name']
        )
        items.append(item)

    return items


async def insert_item_into_database(item: InventoryItem) -> None:
    # set up database connection
    conn = await asyncpg.connect(user=settings.POSTGRES_USER, password=settings.POSTGRES_PASSWORD,
                                  database=settings.POSTGRES_DB, host=settings.POSTGRES_HOST, port=settings.POSTGRES_PORT)

    # execute SQL query to insert new item into table
    query = 'INSERT INTO inventoryitem (name, price, image, description, brand, currentInventory, id) VALUES ($1, $2, $3, $4, $5, $6, $7)'

    try:
        result = await conn.execute(query, item.name, item.price, item.image, item.description, item.brand, item.currentInventory, item.id)
    except asyncpg.exceptions.PostgresError as e:
        await conn.close()
        raise HTTPException(status_code=500, detail=f"Failed to insert item into database: {e}")

    # close database connection
    await conn.close()

async def get_items_by_user(user_name: str) -> List[InventoryItem]:
    # set up database connection
    print("connecting to database")
    conn = await asyncpg.connect(user=settings.POSTGRES_USER, password=settings.POSTGRES_PASSWORD,
                                  database=settings.POSTGRES_DB, host=settings.POSTGRES_HOST, port=settings.POSTGRES_PORT)

    # execute SQL query to retrieve items for the given user name
    print("running query")
    query = 'SELECT * FROM inventoryitem WHERE user_name = $1'
    rows = await conn.fetch(query, user_name)

    # close database connection
    await conn.close()

    # if no items found, return empty list
    if not rows:
        return []

    # create and return list of InventoryItem objects
    items = []
    for row in rows:
        item = InventoryItem(
            name=row['name'],
            price=row['price'],
            image=row['image'],
            description=row['description'],
            brand=row['brand'],
            currentInventory=row['currentinventory'],
            id=row['id'],
            user_name=row['user_name']
        )
        items.append(item)

    return items
