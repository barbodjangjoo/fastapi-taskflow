from app.models.task import Task
from app.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: str | None = None, is_completed: bool = False) -> Task:
        
        return self.repository.create(title=title, description=description, is_completed=is_completed)

    def get_task(self, task_id: int) -> Task | None:

        return self.repository.get_by_id(task_id)
    