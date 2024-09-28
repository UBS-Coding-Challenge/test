from fastapi import APIRouter, status

from src.questions.q5_efficient_hunter_kazuma.request import Q5Request
from src.questions.q5_efficient_hunter_kazuma.response import Q5Response
from src.questions.q5_efficient_hunter_kazuma.solution import \
    q5_efficient_hunter_kazuma
from typing import List

router = APIRouter()

# Request body
@router.post("/efficient-hunter-kazuma", status_code=status.HTTP_200_OK)
async def q5(request: List[Q5Request]):
    res = []
    for req in request:
        efficiency = q5_efficient_hunter_kazuma(req.monsters)
        res.append(Q5Response(efficiency=efficiency))
    return res