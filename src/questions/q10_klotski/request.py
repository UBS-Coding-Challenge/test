from pydantic import BaseModel, Field

class Q10Request(BaseModel):
    board: str = Field(...)
    moves: str = Field(...)