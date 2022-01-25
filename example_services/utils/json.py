import logging
from typing import Any
import orjson
from collections import OrderedDict
import asyncpg.pgproto.pgproto
from starlette.responses import JSONResponse
import sqlalchemy

logger = logging.getLogger(__name__)

def default(obj):
    if isinstance(obj, sqlalchemy.engine.RowMapping):
        result = {}
        try:
            for key in obj.keys():
                result[str(key)] = getattr(obj, key)
            return result
        except Exception as e:
            logger.error('Failed to parse obj due to exception {}'.format(e))
            raise Exception('Failed to parse obj in default')
    raise TypeError

class OrjsonResponse(JSONResponse):
    media_type = 'application/vnd.api+json'

    def render(self, content: Any) -> bytes:
        if content is None:
            return b''
        return orjson.dumps(content, default=default)