from fastapi import APIRouter, status

from src.questions.q10_klotski.request import Q10Request
from src.questions.q10_klotski.solution import q10_klotski
from src.questions.q1_bobby_bug.request import Q1Request
from src.questions.q1_bobby_bug.solution import q1_solution
from src.questions.q5_efficient_hunter_kazuma.request import Q5Request
from src.questions.q5_efficient_hunter_kazuma.response import Q5Response
from src.questions.q5_efficient_hunter_kazuma.solution import \
    q5_efficient_hunter_kazuma
from typing import List

router = APIRouter()

# Request body
@router.post("/bugfixer/p2", status_code=status.HTTP_200_OK)
async def q5(request: List[Q1Request]):
    res = []
    for req in request:
        res.append(q1_solution(req.bugseq))
    return res
