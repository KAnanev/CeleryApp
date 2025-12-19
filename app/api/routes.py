from fastapi import APIRouter

from core.schemas import TaskResponse, TaskRequest
from tasks.demo import add

router = APIRouter()

@router.post('/tasks', response_model=TaskResponse)
async def create_task(payload: TaskRequest) -> TaskResponse:
    result = add.delay(payload.first, payload.second)
    return TaskResponse(task_id=result.id)
