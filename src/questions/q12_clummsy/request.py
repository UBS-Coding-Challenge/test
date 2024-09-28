from pydantic import BaseModel, Field

class Q12Request(BaseModel):
    dictionary: list[str] = Field(...)
    mistypes: list[str] = Field(...)