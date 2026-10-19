
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import check_db_connection
from app.routers.tasks import router as tasks_router


app = FastAPI(
    title="Taskflow API",
    description="A task management API built with FastAPI and PostgreSQL",
    version="1.0.0",
)


# Register routers
app.include_router(tasks_router)


@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Taskflow API is running"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"message": "ok"}


@app.get("/health/db", tags=["Health"])
def database_health_check():
    try:
        check_db_connection()
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )

    return {"database": "ok"}
