class ProductService:
    def __init__(self, repo):
        self.repo = repo

    async def create_product(self, name):
        return await self.repo.create(name)

    async def get_products(self):
        return await self.repo.get_all()

    async def update_product(self, product_id, name):
        return await self.repo.update(product_id, name)

    async def delete_product(self, product_id):
        return await self.repo.delete(product_id)