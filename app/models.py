from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    description = Column(String(length=255))
    price = Column(Float(asdecimal=True, precision=2))
