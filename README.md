# Example Python API project using Starlette and SQLAlchemy Core with asyncpg

This is a template project using [Starlette](https://www.starlette.io/) (a lightweight ASGI framework), [SQLAlchemy Core](https://docs.sqlalchemy.org/en/14/core/) (not ORM), [asyncpg](https://magicstack.github.io/asyncpg/current/) (database interface for PostgreSQL and Python/asyncio). For fast JSON serioalizaiton project uses [orjson](https://github.com/ijl/orjson).

# Prerequisite
Project setup requires [Pyenv](https://github.com/pyenv/pyenv) and [Poetry](https://python-poetry.org/).

```
pyenv install 3.10.1
pyenv local 3.10.1
pyenv global 3.10.1
poetry env use 3.10.1
poetry install
poetry shell
```

# Running Project
Change directory to project,

```
cd example-services
```

Apply migration,

```
alembic upgrade head
```

In local run with uvicorn,

```
uvicorn example_services:app --port 8080 --log-config logger.json --log-level error
```

In production run with Gunicorn and Nginx as reverse proxy,

```
gunicorn --log-level error -w 4 -k uvicorn.workers.UvicornWorker example_services:app
```

# Performnce Considerations
Maximum mumber of PostgreSQL database connections seems to be a key performance bottleneck in our load testing (see details below).

Find max number of connections supported by PostgreSQL instance,

```
SELECT * FROM pg_settings WHERE name = 'max_connections';
```

You can change the number of max DB connections if running self-managed PostgreSQL instance. If you are using the cloud-based PostgreSQL instance RDS or something similar, max number of connections is dictated by instance size as set by cloud provider.

Find number of connections currently active,

```
SELECT sum(numbackends) FROM pg_stat_database;
```

# Performance Benchmarks
We ran performance benchmarks on `MacBook (Retina, 12-inch, Early 2016)` which comes with 1.1 GHz Dual-Core Intel Core m3 and 8 GB 1867 MHz LPDDR3.

We used PostgreSQL(14.1) installed on Macbook and modified max number of connections `200`.
