from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str

class ProductRead(ProductCreate):
    id: int

    class Config:
        from_attributes = True