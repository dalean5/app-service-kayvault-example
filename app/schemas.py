from decimal import Decimal

from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    description: str
    price: Decimal

    class Config:
        orm_mode = True


class ProductOut(ProductIn):
    id: int
