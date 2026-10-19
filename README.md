# ⚡ FastAPI Taskflow

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-0.143+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange.svg?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

<p align="center">
  <strong>A high-performance, containerized REST API engineered with FastAPI, PostgreSQL 16, and SQLAlchemy 2.0 — implementing Clean Layered Architecture and Alembic schema migrations.</strong>
</p>

[Explore Docs](#-interactive-api-documentation) •
[Architecture](#-architecture--design-patterns) •
[Quickstart](#-quick-start) •
[API Reference](#-api-endpoints) •
[Roadmap](#-roadmap)

</div>

---

## 📖 Overview

**FastAPI Taskflow** is a production-oriented Task Management service built from the ground up following clean software engineering principles. It separates web routing, domain business logic, and database persistence into decoupled, testable layers.

Whether running locally or deployed via Docker Compose, it provides out-of-the-box database health checks, connection pooling, automated schema migrations, and OpenAPI-compliant interactive documentation.

---

## ✨ Features

- 🏗️ **Clean Layered Architecture**: Strict separation of concerns (**Routers → Services → Repositories → Models/Database**).
- ⚡ **High-Performance Asynchronous Base**: Powered by **FastAPI**, **Starlette**, and ASGI server **Uvicorn**.
- 🗄️ **Modern Persistence**: **SQLAlchemy 2.0** with strict type-annotated `Mapped[...]` syntax and `psycopg3` driver.
- 📦 **Database Versioning**: Version-controlled migrations powered by **Alembic**.
- 🐳 **Docker-First Workflow**: Seamless local orchestration via **Docker** and **Docker Compose** with database readiness healthchecks.
- 🩺 **Deep Health Checks**: Built-in `/health` (app status) and `/health/db` (live DB ping) endpoints ready for orchestration platforms (Kubernetes / ECS).
- 🛡️ **Schema Validation**: Robust input parsing, data sanitation, and serialization using **Pydantic v2**.
- 📖 **Interactive API Documentation**: Auto-generated **Swagger UI** and **ReDoc** documentation.

---

## 🏛 Architecture & Design Patterns

The project follows a **Layered (N-Tier) Architecture** with Dependency Injection to ensure high testability, maintainability, and clean separation of concerns:

```mermaid
graph TD
    Client([HTTP Client / Frontend])
    
    subgraph FastAPI Application
        Router["Routers / Controllers<br/><code>app/routers/</code>"]
        Dependency["Dependency Injection<br/><code>app/dependencies.py</code>"]
        Service["Service Layer (Business Logic)<br/><code>app/services/</code>"]
        Repository["Repository Layer (Data Access)<br/><code>app/repositories/</code>"]
        Schema["Pydantic Schemas<br/><code>app/schemas/</code>"]
    end
    
    subgraph Persistence Layer
        Model["SQLAlchemy ORM Models<br/><code>app/models/</code>"]
        DB[(PostgreSQL 16)]
    end

    Client -->|HTTP Request / JSON| Router
    Router -.-> Schema
    Router -->|Calls| Service
    Dependency -.->|Provides Session & Services| Router
    Service -->|Queries / Persists via| Repository
    Repository -->|Interacts with| Model
    Model -->|Executes SQL| DB
    DB -->|Result Sets| Model
    Repository -->|Domain Entities| Service
    Service -->|Domain Objects| Router
    Router -->|JSON Response| Client
```

### Module Organization

```text
fastapi-taskflow/
├── alembic/                  # Alembic migration environment and versions
│   ├── versions/             # Timestamped database revision scripts
│   └── env.py                # Alembic runtime configuration
├── app/
│   ├── db/                   # Database engine, session maker, & Base class
│   │   ├── base.py           # Declarative base model
│   │   └── session.py        # SQLAlchemy engine and connection pool
│   ├── models/               # SQLAlchemy ORM entity definitions
│   │   └── task.py           # Task database model
│   ├── repositories/         # Data Access Object (DAO) / Repository pattern
│   │   └── task_repository.py# Database CRUD operations
│   ├── services/             # Domain business logic & orchestrations
│   │   └── task_service.py   # Task business operations
│   ├── routers/              # API endpoints and HTTP route declarations
│   │   └── tasks.py          # /tasks routing
│   ├── schemas/              # Pydantic models for validation and serialization
│   │   └── task.py           # TaskCreate & TaskResponse schemas
│   ├── dependencies.py       # FastAPI dependency injection providers
│   └── main.py               # FastAPI entrypoint, middleware, & health probes
├── docker-compose.yaml       # Multi-container service definitions
├── Dockerfile                # Lightweight Python 3.11 image configuration
├── alembic.ini               # Alembic database configuration
├── requirements.txt          # Frozen application dependencies
├── .env.example              # Sample environment variables
└── README.md                 # Project documentation
```

---

## 🛠 Tech Stack

| Technology | Role | Purpose |
| :--- | :--- | :--- |
| **Python 3.11+** | Language | Modern typing, high speed, and reliability |
| **FastAPI** | Web Framework | Modern, high-performance async REST API framework |
| **PostgreSQL 16** | Database | ACID-compliant relational data store |
| **SQLAlchemy 2.0** | ORM | Type-safe declarative database operations |
| **Psycopg 3** | DB Driver | Next-generation PostgreSQL driver for Python |
| **Alembic** | Migrations | Deterministic, version-controlled schema evolutions |
| **Pydantic v2** | Data Validation | High-throughput schema enforcement and serialization |
| **Docker & Compose** | Containerization | Consistent multi-container development and deployment |
| **Uvicorn** | ASGI Server | Lightning-fast asynchronous server implementation |

---

## 🚀 Quick Start

You can get the application up and running either using **Docker Compose** (recommended) or **locally in a virtual environment**.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/) **OR**
- [Python 3.11+](https://www.python.org/) and a running [PostgreSQL](https://www.postgresql.org/) instance.

---

### Option 1: Running with Docker Compose (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/barbodjangjoo/fastapi-taskflow.git
   cd fastapi-taskflow
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```

3. **Start the containers:**
   ```bash
   docker compose up --build
   ```

4. **Apply database migrations:**
   Open a separate terminal and run:
   ```bash
   docker compose exec api alembic upgrade head
   ```

5. The API will now be live at **`http://localhost:8000`**!

---

### Option 2: Local Manual Setup

1. **Clone and enter repository:**
   ```bash
   git clone https://github.com/barbodjangjoo/fastapi-taskflow.git
   cd fastapi-taskflow
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Setup environment variables:**
   Create a `.env` file pointing to your PostgreSQL instance:
   ```env
   POSTGRES_DB=taskflow_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/taskflow_db
   ```

5. **Run Alembic migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Start the development server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 📚 Interactive API Documentation

Once the server is running, explore the interactive documentation powered by OpenAPI:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI Schema (JSON)**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 📡 API Endpoints

### 🩺 System & Health Checks

| Method | Endpoint | Description | Expected Response |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root greeting | `{"message": "Taskflow API is running"}` |
| `GET` | `/health` | Liveness check (Application) | `{"message": "ok"}` |
| `GET` | `/health/db` | Readiness check (PostgreSQL) | `{"database": "ok"}` |

### 📋 Task Management

| Method | Endpoint | Status | Description |
| :--- | :--- | :--- | :--- |
| `GET` | `/tasks` | `200 OK` | Retrieve all tasks |
| `GET` | `/tasks/{task_id}` | `200 OK` | Retrieve a specific task by ID (or `404`) |
| `POST` | `/tasks` | `201 Created` | Create a new task |

#### Example: Create a Task

**Request (`POST /tasks`):**
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Design Database Schema",
    "description": "Finalize models and foreign key constraints",
    "completed": false
  }'
```

**Response (`201 Created`):**
```json
{
  "id": 1,
  "title": "Design Database Schema",
  "description": "Finalize models and foreign key constraints",
  "completed": false
}
```

#### Example: Fetch Task by ID

**Request (`GET /tasks/1`):**
```bash
curl -X GET "http://localhost:8000/tasks/1"
```

**Response (`200 OK`):**
```json
{
  "id": 1,
  "title": "Design Database Schema",
  "description": "Finalize models and foreign key constraints",
  "completed": false
}
```

---

## 🗃️ Database Migrations (Alembic)

Schema management is handled declaratively with **Alembic**:

```bash
# Create a new migration revision after modifying models
alembic revision --autogenerate -m "describe_changes"

# Apply pending migrations to the latest revision
alembic upgrade head

# Rollback the last migration
alembic downgrade -1

# View migration history
alembic history --verbose
```

---

## ⚙️ Environment Configuration

| Variable | Type | Default / Example | Purpose |
| :--- | :--- | :--- | :--- |
| `POSTGRES_DB` | `string` | `taskflow_db` | PostgreSQL database name |
| `POSTGRES_USER` | `string` | `taskflow_user` | PostgreSQL administrative user |
| `POSTGRES_PASSWORD` | `string` | `change_this_dev_password` | PostgreSQL user password |
| `DATABASE_URL` | `string` | `postgresql+psycopg://...` | Database connection DSN |

---

## 🗺️ Roadmap

- [ ] **Full CRUD**: Add `PUT/PATCH /tasks/{id}` (update) and `DELETE /tasks/{id}` endpoints.
- [ ] **Filtering & Pagination**: Add query parameters (`?status=completed&limit=20&offset=0`).
- [ ] **Authentication & Authorization**: Implement JWT-based user authentication and multi-tenancy.
- [ ] **Automated Testing Suite**: Full test coverage with `pytest`, `httpx.AsyncClient`, and Testcontainers.
- [ ] **Caching Layer**: Integrate Redis for high-frequency queries.
- [ ] **CI/CD Pipeline**: GitHub Actions workflow for linting (Ruff/Black), typing (Mypy), and tests.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/barbodjangjoo/fastapi-taskflow/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">
  Developed with ❤️ by <a href="https://github.com/barbodjangjoo"><strong>Barbod Jangjoo</strong></a>
</div>