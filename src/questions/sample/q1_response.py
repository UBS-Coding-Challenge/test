from pydantic import BaseModel, Field

class Q1Response(BaseModel):
    res: int = Field(...)