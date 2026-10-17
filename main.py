from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Taskflow API is running"}

@app.get("/health")
def health_check():
    return {"message": "ok"}