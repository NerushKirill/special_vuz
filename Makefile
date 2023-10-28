app:
	poetry run uvicorn backend.src.main:app --reload --host 127.0.0.1 --port 8000