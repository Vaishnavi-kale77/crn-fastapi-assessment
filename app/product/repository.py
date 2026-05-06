from app.product.models import Product
from sqlalchemy import select

class ProductRepository:
    def __init__(self, db):
        self.db = db

    async def create(self, name):
        product = Product(product_name=name)
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        return product

    async def get_all(self):
        result = await self.db.execute(select(Product))
        return result.scalars().all()

    async def update(self, product_id, name):
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()

        if not product:
            return None

        product.product_name = name
        await self.db.commit()
        await self.db.refresh(product)
        return product

    async def delete(self, product_id):
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        product = result.scalar_one_or_none()

        if not product:
            return False

        await self.db.delete(product)
        await self.db.commit()
        return True