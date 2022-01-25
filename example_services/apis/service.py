from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
from starlette import status
from example_services.logger import getLogger

logger = getLogger(__name__)

class Root(HTTPEndpoint):
    async def api_name(request):
        return JSONResponse({'name': 'core-serivces'})

    async def api_version(request):
        return JSONResponse({'version': 'v1'})