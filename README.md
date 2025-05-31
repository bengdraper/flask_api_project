
# Flask API Project ERP

## File System Overview

```
flask_api_project_erp/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── wsgi.py
├── instance/
├── migrations/
└── src/
    ├── __init__.py
    ├── db.py
    ├── api/
    └── models/
```

## Setup & Usage

### 1. Prerequisites
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- Or: Python 3.10+ and pip (for local development)

docker compose build
docker compose up
docker compose exec flask_api alembic upgrade head

### 2. Running with Docker Compose (Standalone)

From the project root (`flask_api_project_erp/`):

```bash
docker compose build
docker compose up
```

- The Flask API will be available at `http://localhost:5001` (see `docker-compose.yml`).
- The PostgreSQL database will be available at `localhost:5435`.

#### Database Migrations (Docker)
To run Alembic migrations inside the container:
```bash
docker compose exec flask_api alembic upgrade head
```

### 3. Running Locally with Python Virtual Environment

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Set environment variables as needed (see `instance/` or `.env.example`).
   - You may need to customize database connection strings and Flask settings.
3. Start a local PostgreSQL database (see `docker-compose.yml` for settings, or use your own).
4. Run the Flask app:
   ```bash
   flask run --host=0.0.0.0 --port=5001
   ```

## API Endpoints
- See `src/api/` for available endpoints

