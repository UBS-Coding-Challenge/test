from pydantic import BaseModel, Field

class Q5Request(BaseModel):
    monsters: list[int] = Field(...)