from pydantic import BaseModel, Field

class Q1Request(BaseModel):
    name: str = Field(default=...)
    age: int = Field(default=...)
    nums: list[int] = Field(default=...)
    nickname: str = Field(default=None)