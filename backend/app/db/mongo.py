from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client: AsyncIOMotorClient | None = None

def get_client() -> AsyncIOMotorClient:
    global client
    if client is None:
        client = AsyncIOMotorClient(settings.DATABASE_URL)
    return client

def get_db():
    return get_client()[settings.DB_NAME]

async def close_client():
    global client
    if client is not None:
        client.close()
        client = None
