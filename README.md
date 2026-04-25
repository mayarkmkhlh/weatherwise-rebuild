# weatherwise-rebuild

Current status: early rebuild bootstrap is done; core WeatherWise features are not implemented yet.

## What has been done so far

- Repository initialized with separate `backend`, `frontend`, and root-level project files.
- Frontend scaffold created with Vite + React + TypeScript.
- Backend scaffold created with FastAPI and a minimal app entrypoint.
- Basic backend dependency list added in `requirements.txt`.
- A starter backend test file was added (`backend/test_basic.py`).
- A broad `.gitignore` is already in place for Python/node/temp artifacts.

## What is currently working

- Backend exposes a health check endpoint:
  - `GET /health` returns `{ "status": "ok" }`
- Frontend has the default Vite TypeScript template setup.
- Frontend package scripts exist for:
  - `dev`
  - `build`
  - `lint`
  - `preview`

## What is not done yet (next steps)

- No WeatherWise domain endpoints yet (no `/predict`, `/auth`, `/reports`, `/chat`).
- No backend architecture layers yet (`routers/services/models/core` structure is still pending).
- No weather API integration or normalization pipeline yet.
- No recommendation logic (rule-based or ML-backed) yet.
- No database setup, migrations, or auth/JWT flows yet.
- No shared typed API contract wired between backend schemas and frontend types yet.
- No ML training/artifact/versioning pipeline in this rebuild repo yet.
- No CI pipeline or release flow configured yet.

## Current file-level snapshot

- `backend/main.py`: minimal FastAPI app with `/health`.
- `backend/test_basic.py`: placeholder passing test.
- `frontend/package.json`: Vite + React + TypeScript dependencies and scripts.
- `frontend/README.md`: default template README (not project-specific yet).
- `requirements.txt`: minimal FastAPI/uvicorn/pydantic stack dependencies.

## Immediate recommended next milestone

Implement the first vertical slice end-to-end:

1. Add backend `POST /predict` (initially rule-based).
2. Add typed frontend API call + simple recommendation UI.
3. Keep `GET /health` and add one integration test for `/predict`.

That gives a real working baseline before auth/community/chat/ML phases.

## Setup
git clone <repo>
cd weatherwise-rebuild

# Environment Variables
cp .env.example .env

# Backend
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# Frontend
cd frontend
npm install