from pydantic import BaseModel, Field

class Q3Request(BaseModel):
    time: list[int] = Field(...)
    prerequisites: list[tuple] = Field(...)