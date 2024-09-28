from pydantic import BaseModel, Field

class Q2Response(BaseModel):
    instructions: list[str] | None = Field(default=None)