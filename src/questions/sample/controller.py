from fastapi import APIRouter, status
from src.questions.sample.q1_request import Q1Request
from src.questions.sample.q1_response import Q1Response
from src.questions.sample.q1_service import q1_get_sum

router = APIRouter(tags=['sample'])

# Simplest
@router.get("/sample", status_code=status.HTTP_200_OK)
async def sample1():
    return {'hello': "hello"}

# Path parameter
@router.get("/sample/path/{sample_id}", status_code=status.HTTP_200_OK)
async def sample_path(sample_id: int):
    return {'hello': 'hello'}

# Query Params
@router.get("/sample/query-param", status_code=status.HTTP_200_OK)
async def sample_query_param(name: str, age: int | None = None):
    print(name)
    print(age)
    return {'name': name, 'age': age}

# Request body
@router.post("/samples", status_code=status.HTTP_201_CREATED)
async def create_sample(request: Q1Request) -> Q1Response:
    res = q1_get_sum(request.nums, 10)
    print("hello")
    return Q1Response(res=res)