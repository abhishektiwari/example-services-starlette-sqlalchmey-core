from example_services.config import ASYNC_DATABASE_URL, ASYNC_POOL_SIZE
from sqlalchemy.ext.asyncio import create_async_engine

async_engine = create_async_engine(
    f"{ASYNC_DATABASE_URL}",
    future=True,
    echo=False,
    pool_size=ASYNC_POOL_SIZE,
    max_overflow=5,
    pool_timeout=60
)

