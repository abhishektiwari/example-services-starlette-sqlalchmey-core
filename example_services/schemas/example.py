from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

class Example(BaseModel):
    id: UUID = Field(
        title="Id",
        description="",
    )
    name: str = Field(
        title="name",
        description="",
    )
    description: str = Field(
        title="description",
        description="",
    )
    created_at: datetime = Field(
        title="created_at",
        description="",
    )
    updated_at: datetime = Field(
        title="updated_at",
        description="",
    )

class Examples(BaseModel):
    __root__: List[Example]