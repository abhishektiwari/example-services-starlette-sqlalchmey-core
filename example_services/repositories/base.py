from example_services.database import database

class SqlAlchemyRepository:
    async def bulk_insert(self, query, values):
        async with database.transaction():
            await database.execute(query=query, values=values)
        return values

    async def bulk_insert(self, query, values):
        async with database.transaction():
            await database.execute_many(query=query, values=values)
        return values

    async def delete(self, query):
        async with database.transaction():
            result = await database.execute(query)
            if result.rowcount == 0:
                raise Exception("Failed to delete")

    async def get_one(self, query):
        async with database.transaction():
            result = await database.fetch_one(query=query)
            if not result:
                raise Exception("No such record")
            return result

    async def get_all(self, query):
        async with database.transaction():
            return await database.fetch_all(query=query)