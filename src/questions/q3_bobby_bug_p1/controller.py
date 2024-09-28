from fastapi import APIRouter, status

from src.questions.q13_digital_colony.request import Q13Request
from src.questions.q1_bobby_bug.request import Q1Request
from src.questions.q1_bobby_bug.solution import q1_solution
from typing import List

from src.questions.q3_bobby_bug_p1.request import Q3Request
from src.questions.q3_bobby_bug_p1.solution import q3_solution

router = APIRouter()

# Request body
@router.post("/bugfixer/p1", status_code=status.HTTP_200_OK)
async def q3(request: List[Q3Request]):
    res = []
    for req in request:
        res.append(q3_solution(req.time, req.prerequisites))
    return res
