import logging
from starlette.endpoints import HTTPEndpoint
from starlette import status
from example_services.utils.json import OrjsonResponse
from example_services.database import async_engine
from example_services.tables.examples import examples

logger = logging.getLogger(__name__)

class ExampleListCreateAPIView(HTTPEndpoint):
    async def get(self, req):
        results = []
        page = 0
        page_size = 5
        if "page" in req.query_params:
            try:
                page = int(req.query_params["page"])
            except ValueError:
                page = 0

        query = (
            examples.select()
            .limit(page_size)
            .offset(page * page_size)
            .with_only_columns(
                examples.c.uuid,
                examples.c.name,
                examples.c.description,
                examples.c.created_at,
                examples.c.updated_at,
            )
        )
        async with async_engine.connect() as conn:
            results = await conn.execute(query)
            data = results.mappings().all()
            await conn.close()
        return OrjsonResponse(data, status_code=status.HTTP_200_OK
        )

    async def post(self, req):
        result = {}
        values = await req.json()
        query = examples.insert().returning(
            examples.c.uuid,
            examples.c.name,
            examples.c.description,
            examples.c.created_at,
            examples.c.updated_at,
        )
        async with async_engine.connect() as conn:
            result = await conn.execute(query, values)
            await conn.commit()
            data = result.mappings().fetchone()
            await conn.close()
            
        return OrjsonResponse(data, status_code=status.HTTP_201_CREATED)


class ExampleRetrieveUpdateDestroyAPIView(HTTPEndpoint):
    async def get(self, req):
        uuid = req.path_params["uuid"]
        query = (
            examples.select()
            .where(examples.c.uuid == uuid)
            .with_only_columns(
                examples.c.uuid,
                examples.c.name,
                examples.c.description,
                examples.c.created_at,
                examples.c.updated_at,
            )
        )
        result = await async_database.fetch_one(query=query)
        if result == None:
            return OrjsonResponse({}, status_code=status.HTTP_400_BAD_REQUEST)
        return OrjsonResponse(dict(result), status_code=status.HTTP_200_OK)

    async def patch(self, req):
        uuid = req.path_params["uuid"]
        query = (
            examples.update()
            .where(examples.c.uuid == uuid)
            .returning(
                examples.c.uuid,
                examples.c.name,
                examples.c.description,
                examples.c.created_at,
                examples.c.updated_at,
            )
        )
        values = await req.json()
        result = await async_database.fetch_one(query=query, values=values)
        return OrjsonResponse(dict(result), status_code=status.HTTP_200_OK)

    async def delete(self, req):
        uuid = req.path_params["uuid"]
        query = examples.delete().where(examples.c.uuid == uuid)
        result = await async_database.execute(query)
        return OrjsonResponse("", status_code=status.HTTP_204_NO_CONTENT)
