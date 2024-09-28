from fastapi import APIRouter, status

from src.questions.q10_klotski.request import Q10Request
from src.questions.q10_klotski.solution import q10_klotski
from src.questions.q13_digital_colony.request import Q13Request
from src.questions.q13_digital_colony.solution import q13_solution
from typing import List

router = APIRouter()

# Request body
@router.post("/digital-colony", status_code=status.HTTP_200_OK)
async def q13(request: List[Q13Request]):
    res = []
    for req in request:
        weight = q13_solution(req.generations, req.colony)
        res.append(weight)
    return res
