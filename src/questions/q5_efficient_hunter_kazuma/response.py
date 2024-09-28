from pydantic import BaseModel, Field

class Q5Response(BaseModel):
    efficiency: int = Field(...)