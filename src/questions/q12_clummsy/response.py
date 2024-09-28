from pydantic import BaseModel, Field

class Q12Response(BaseModel):
    corrections: list[str] = Field(...)