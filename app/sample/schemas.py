from datetime import date
from pydantic import BaseModel, Field

class CreateSampleSchema(BaseModel):
    sku: str = Field(default=None, max_length=15, min_length=1)
    name: str = Field(default=None, min_length=1)
    method: str | None = Field(default=None, max_length=1024)
    created_at: date

