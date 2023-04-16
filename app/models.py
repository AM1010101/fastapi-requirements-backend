from pydantic import BaseModel

class InventoryItem(BaseModel):
    name: str
    price: str
    image: str
    description: str
    brand: str
    currentInventory: int
    id: str
    user_name: str
