from starlette.applications import Starlette
from example_services.routes import routes
from example_services.logger import getLogger
from example_services.database import async_engine

logger = getLogger(__name__)
app = Starlette(routes=routes, debug=True)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    # await async_database.connect()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await async_engine.dispose()
    # await async_database.disconnect()