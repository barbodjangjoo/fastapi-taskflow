from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_task_service
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=list[TaskResponse])
def list_tasks(
    service: TaskService = Depends(get_task_service),
):
    return service.get_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
):
    task = service.get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task


@router.post("", response_model=TaskResponse, status_code=201)
def create_task(
    task_data: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    return service.create_task(
        title=task_data.title,
        description=task_data.description,
        is_completed=task_data.completed,
    )