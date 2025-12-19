from pydantic import BaseModel


class TaskRequest(BaseModel):
    first: int
    second: int
    request_id: str


class TaskResponse(BaseModel):
    task_id: str
