import databases
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=False)
SECRET_KEY = config('SECRET_KEY', cast=Secret)
ASYNC_DATABASE_URL = config('ASYNC_DATABASE_URL', cast=databases.DatabaseURL)
SYNC_DATABASE_URL = config('SYNC_DATABASE_URL', cast=databases.DatabaseURL)
ASYNC_POOL_SIZE=config('ASYNC_POOL_SIZE', cast=int, default=99)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings)