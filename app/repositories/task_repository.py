from app.models import task
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    
    def create(self, title: str, description: str | None = None, is_completed: bool = False) -> Task:
        
        task = Task(title=title, description=description, is_completed=is_completed)
        
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def get_by_id(self, task_id: int) -> Task | None:
        
        statement = select(Task).where(Task.id == task_id)

        return self.db.scalars(statement).first()

    def get_all(self) -> list[Task]:

        statement = select(Task).order_by(Task.id)

        return list(self.db.scalars(statement).all())

    def update(self, task: Task, data: dict) -> Task:
        for field, value in data.items():
            setattr(task, field, value)

        self.db.commit()
        self.db.refresh(task)

        return task
    

