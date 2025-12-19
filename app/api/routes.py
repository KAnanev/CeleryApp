from fastapi import APIRouter
from tasks.demo import add

router = APIRouter()

@router.post('/tasks')
async def root():
    result = add.delay(2,3)
    return {'message': f'{result}'}
