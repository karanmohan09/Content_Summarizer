from app.api import app
# Run with: uvicorn main:app --reload

# This file simply exposes the FastAPI `app` object
# so Uvicorn (or Docker) can run it like: uvicorn main:app --reload

# To run locally:
# uvicorn main:app --reload

# To run in Docker (API mode):
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
