from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

from app.auth.security import create_access_token
from app.product.router import router as product_router

app = FastAPI(title="CRN Product API")


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
def root():
    return {"message": "API is running successfully 🚀"}


@app.post("/login")
async def login():
    user_data = {"sub": "admin"}
    token = create_access_token(user_data)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ✅ REGISTER ROUTER
app.include_router(product_router)