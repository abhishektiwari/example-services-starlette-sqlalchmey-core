import uuid
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

metadata = sqlalchemy.MetaData()

examples = sqlalchemy.Table(
    "examples",
    metadata,
    sqlalchemy.Column("uuid", UUID, primary_key=True, unique=True, nullable=False, server_default=func.uuid_generate_v4()),
    sqlalchemy.Column("name", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(length=300), nullable=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, nullable=False, server_default=func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, nullable=False, server_default=func.now(), server_onupdate=func.now())
)
