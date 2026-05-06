from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.product.schemas import ProductCreate, ProductRead
from app.product.repository import ProductRepository
from app.product.service import ProductService
from app.auth.dependencies import get_current_user  # 👈 ADD

router = APIRouter(prefix="/products", tags=["products"])


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/", response_model=ProductRead)
async def create_product(
    data: ProductCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)  # 👈 ADD
):
    service = ProductService(ProductRepository(db))
    return await service.create_product(data.product_name)


@router.get("/", response_model=list[ProductRead])
async def get_products(
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)  # 👈 ADD
):
    service = ProductService(ProductRepository(db))
    return await service.get_products()


@router.put("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: int,
    data: ProductCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)  # 👈 ADD
):
    service = ProductService(ProductRepository(db))
    return await service.update_product(product_id, data.product_name)


@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)  # 👈 ADD
):
    service = ProductService(ProductRepository(db))
    return await service.delete_product(product_id)