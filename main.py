from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

tasks = {}


class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str 
    completed: bool



@app.get("/")
def read_root():
    return {"message": "Taskflow API is running"}



@app.get("/health")
def health_check():
    return {"message": "ok"}



@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task   



@app.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    return list(tasks.values())



@app.post("/tasks", response_model=TaskResponse)
def create_tasks(task: TaskCreate):

    task_id = len(tasks) + 1

    task_response = TaskResponse(
        id=task_id,
        title = task.title,
        description=task.description,
        completed= task.completed
    )
    tasks[task_id] = task_response.model_dump()
    print(tasks)
    return task_response