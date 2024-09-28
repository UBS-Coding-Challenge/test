from fastapi import APIRouter, status

from src.questions.q10_klotski.request import Q10Request
from src.questions.q10_klotski.solution import q10_klotski
from src.questions.q5_efficient_hunter_kazuma.request import Q5Request
from src.questions.q5_efficient_hunter_kazuma.response import Q5Response
from src.questions.q5_efficient_hunter_kazuma.solution import \
    q5_efficient_hunter_kazuma
from typing import List

router = APIRouter()

# Request body
@router.post("/klotski", status_code=status.HTTP_200_OK)
async def q5(request: List[Q10Request]):
    res = []
    for req in request:
        res_str = q10_klotski(req.board, req.moves)
        res.append(res_str)
    return res
