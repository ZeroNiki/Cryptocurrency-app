from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from operation.router import router as router_operation
from pages.router import router as router_page

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead

from redis import asyncio as aioredis


app = FastAPI(
    title="Cryptocurrency"
)

# Static
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
app.include_router(router_page)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        "redis://redis:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
