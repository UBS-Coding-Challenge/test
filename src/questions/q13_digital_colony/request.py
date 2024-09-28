from pydantic import BaseModel, Field

class Q13Request(BaseModel):
    generations: int = Field(...)
    colony: str = Field(...)