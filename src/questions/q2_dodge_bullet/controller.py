from fastapi import APIRouter, status, Body

from src.questions.q10_klotski.request import Q10Request
from src.questions.q10_klotski.solution import q10_klotski
from src.questions.q1_bobby_bug.request import Q1Request
from src.questions.q1_bobby_bug.solution import q1_solution
from src.questions.q2_dodge_bullet.response import Q2Response
from src.questions.q2_dodge_bullet.solution2 import q2_solution
from src.questions.q5_efficient_hunter_kazuma.request import Q5Request
from src.questions.q5_efficient_hunter_kazuma.response import Q5Response
from src.questions.q5_efficient_hunter_kazuma.solution import \
    q5_efficient_hunter_kazuma
from typing import List
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field
from pprint import pprint
router = APIRouter()

class Response(BaseModel):
    instructi: list[str] = Field(...)

# Request body
@router.post("/dodge", status_code=status.HTTP_200_OK, response_model=Q2Response)
async def q5(grid_str: str = Body()):
    grid = grid_str.split("\n")
    grid = [list(row) for row in grid]
    pprint(grid)
    res = q2_solution(grid)

    print("RESULT")
    print(res)
    return Q2Response(instructions=res)
