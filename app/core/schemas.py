from pydantic import BaseModel


class TaskRequest(BaseModel):
    first: int
    second: int


class TaskResponse(BaseModel):
    task_id: int
