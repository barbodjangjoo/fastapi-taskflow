from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Taskflow API is running"}

@app.get("/health")
def health_check():
    return {"message": "ok"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id, "status": "completed"}