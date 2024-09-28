from pydantic import BaseModel, Field

class Q1Response(BaseModel):
    efficiency: int = Field(...)