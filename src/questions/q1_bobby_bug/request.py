from pydantic import BaseModel, Field

class Q1Request(BaseModel):
    bugseq: list[list[int]] = Field(...)