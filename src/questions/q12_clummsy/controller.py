from fastapi import APIRouter, status

from src.questions.q10_klotski.request import Q10Request
from src.questions.q10_klotski.solution import q10_klotski
from src.questions.q12_clummsy.request import Q12Request
from src.questions.q12_clummsy.response import Q12Response
from src.questions.q12_clummsy.solution import q12_solution
from src.questions.q5_efficient_hunter_kazuma.request import Q5Request
from src.questions.q5_efficient_hunter_kazuma.response import Q5Response
from src.questions.q5_efficient_hunter_kazuma.solution import \
    q5_efficient_hunter_kazuma
from typing import List

router = APIRouter()

# Request body
@router.post("/the-clumsy-programmer", status_code=status.HTTP_200_OK)
async def q5(request: List[Q12Request]):
    res = []
    for req in request:
        # print(len(req.dictionary), len(req.mistypes))
        r = q12_solution(req.dictionary, req.mistypes)
        # print("res", len(r))
        res.append(Q12Response(corrections=r))
    return res
